from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
# getting all lexers from pygment module
LEXERS = [item for item in get_all_lexers() if item[1]]
# getting all languages from pygment module
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Snippet(models.Model):
    """
    A snippet model that is used to store code snippets
    """
    # time at which the code snippet was created
    created = models.DateTimeField(auto_now_add=True)
    # the name of the code snippet
    title = models.CharField(max_length=100, blank=True, default='')
    # the actual code that should be highlighted
    code = models.TextField()
    # the line numbers of the code
    linenos = models.BooleanField(default=False)
    # the type of language the code snippet uses
    language = models.CharField(
        choices=LANGUAGE_CHOICES, default='python', max_length=100)
    # the default styling of the code snippet
    style = models.CharField(choices=STYLE_CHOICES,
                             default='friendly', max_length=100)

    owner = models.ForeignKey(
        'auth.User', related_name='snippets', on_delete=models.CASCADE)
    highlighted = models.TextField()

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)

    class Meta:
        """
        A class that will be used to get the code snippets based on when they were created
        """
        ordering = ('created',)
