from django.db import models

# Create your models here.


class Subject(models.Model):
    name = models.CharField(max_length=30)
    max_points = models.FloatField(null=True)
    my_points = models.FloatField(null=True)

    def __str__(self):
        return self.name

    def percent(self):
        return self.my_points / self.max_points


class Field(models.Model):
    name = models.CharField(max_length=20)
    r1 = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='r1')
    r2 = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='r2')
    p = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='basic')

    def __str__(self):
        return self.name

    def get_g(self):
        output = []
        for item in (self.r1.percent(), self.r2.percent()):
            if item < 30:
                output.append(item)
            elif item <= 80:
                output.append(item + 2 * (item - 30))
            else:
                output.append(item + 100)
        g = 0.75 * output[0] * 0.25 * output[1]
        return g

    def get_m(self):
        return 2 * self.p.percent()

    def get_w(self):
        return 4 * self.get_g() + self.get_m()


