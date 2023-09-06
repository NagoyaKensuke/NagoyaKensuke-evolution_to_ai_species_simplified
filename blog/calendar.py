from calendar import HTMLCalendar
from django.urls import reverse
from .models import Post

class BlogCalendar(HTMLCalendar):
    def __init__(self, year, month, posts):
        super().__init__()
        self.year = year
        self.month = month
        self.posts = self.group_by_day(posts)

    def group_by_day(self, posts):
        field = lambda post: post.published_at.day
        return {day: list(items) for day, items in groupby(posts, field)}

    def formatday(self, day, weekday):
        posts = self.posts.get(day)
        if posts:
            body = ['<ul>']
            for post in posts:
                body.append(f'<li><a href="{reverse("post_detail", args=[post.slug])}">{post.title}</a></li>')
            body.append('</ul>')
            return self.day_cell(weekday, f'{day} {"".join(body)}')
        return self.day_cell(weekday, day)

    def day_cell(self, weekday, value):
        return f'<td class="{self.cssclasses[weekday]}" style="vertical-align: top;">{value}</td>'

    def formatmonth(self, withyear=True):
        return super().formatmonth(self.year, self.month, withyear)
