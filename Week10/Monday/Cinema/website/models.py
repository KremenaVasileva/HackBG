from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=100, unique=True)
    rating = models.FloatField()
    movie_type = models.PositiveSmallIntegerField(default=1)
    cover = models.ImageField()

    def __str__(self):
        return("{} - {}".format(self.name, self.rating))


class Projection(models.Model):
    movie = models.ForeignKey(Movie)

    _2D = 1
    _3D = 2
    _4D = 3
    _4DX = 4

    TYPES = (
             (_2D, '2D'),
             (_3D, '3D'),
             (_4D, '4D'),
             (_4DX, '4DX'),
        )
    projection_type = models.SmallIntegerField(choices=TYPES, default=_2D)

    time = models.DateTimeField()

    def __str__(self):
        return("{} - {} - {}".format(self.movie.name,
                                     self.projection_type,
                                     self.time
                                     )
               )


class Reservation(models.Model):
    username = models.CharField(max_length=30, unique=True)
    projection = models.ForeignKey(Projection)
    row = models.PositiveSmallIntegerField()
    col = models.PositiveSmallIntegerField()

    def __str__(self):
        return("{} - {}, row: {}, col: {}".format(
                                                  self.username,
                                                  self.projection,
                                                  self.row,
                                                  self.col
                                                  )
               )
