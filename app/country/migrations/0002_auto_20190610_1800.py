# Generated by Django 2.2.2 on 2019-06-10 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='alpha2Code',
            field=models.CharField(choices=[('B', 'D'), ('B', 'E'), ('B', 'F'), ('B', 'G'), ('B', 'A'), ('B', 'B'), ('W', 'F'), ('B', 'L'), ('B', 'M'), ('B', 'N'), ('B', 'O'), ('B', 'H'), ('B', 'I'), ('B', 'J'), ('B', 'T'), ('J', 'M'), ('B', 'V'), ('B', 'W'), ('W', 'S'), ('B', 'Q'), ('B', 'R'), ('B', 'S'), ('J', 'E'), ('B', 'Y'), ('B', 'Z'), ('R', 'U'), ('R', 'W'), ('R', 'S'), ('T', 'L'), ('R', 'E'), ('T', 'M'), ('T', 'J'), ('R', 'O'), ('T', 'K'), ('G', 'W'), ('G', 'U'), ('G', 'T'), ('G', 'S'), ('G', 'R'), ('G', 'Q'), ('G', 'P'), ('J', 'P'), ('G', 'Y'), ('G', 'G'), ('G', 'F'), ('G', 'E'), ('G', 'D'), ('G', 'B'), ('G', 'A'), ('S', 'V'), ('G', 'N'), ('G', 'M'), ('G', 'L'), ('G', 'I'), ('G', 'H'), ('O', 'M'), ('T', 'N'), ('J', 'O'), ('H', 'R'), ('H', 'T'), ('H', 'U'), ('H', 'K'), ('H', 'N'), ('H', 'M'), ('V', 'E'), ('P', 'R'), ('P', 'S'), ('P', 'W'), ('P', 'T'), ('S', 'J'), ('P', 'Y'), ('I', 'Q'), ('P', 'A'), ('P', 'F'), ('P', 'G'), ('P', 'E'), ('P', 'K'), ('P', 'H'), ('P', 'N'), ('P', 'L'), ('P', 'M'), ('Z', 'M'), ('E', 'H'), ('E', 'E'), ('E', 'G'), ('Z', 'A'), ('E', 'C'), ('I', 'T'), ('V', 'N'), ('S', 'B'), ('E', 'T'), ('S', 'O'), ('Z', 'W'), ('S', 'A'), ('E', 'S'), ('E', 'R'), ('M', 'E'), ('M', 'D'), ('M', 'G'), ('M', 'F'), ('M', 'A'), ('M', 'C'), ('U', 'Z'), ('M', 'M'), ('M', 'L'), ('M', 'O'), ('M', 'N'), ('M', 'H'), ('M', 'K'), ('M', 'U'), ('M', 'T'), ('M', 'W'), ('M', 'V'), ('M', 'Q'), ('M', 'P'), ('M', 'S'), ('M', 'R'), ('I', 'M'), ('U', 'G'), ('T', 'Z'), ('M', 'Y'), ('M', 'X'), ('I', 'L'), ('F', 'R'), ('I', 'O'), ('S', 'H'), ('F', 'I'), ('F', 'J'), ('F', 'K'), ('F', 'M'), ('F', 'O'), ('N', 'I'), ('N', 'L'), ('N', 'O'), ('N', 'A'), ('V', 'U'), ('N', 'C'), ('N', 'E'), ('N', 'F'), ('N', 'G'), ('N', 'Z'), ('N', 'P'), ('N', 'R'), ('N', 'U'), ('C', 'K'), ('X', 'K'), ('C', 'I'), ('C', 'H'), ('C', 'O'), ('C', 'N'), ('C', 'M'), ('C', 'L'), ('C', 'C'), ('C', 'A'), ('C', 'G'), ('C', 'F'), ('C', 'D'), ('C', 'Z'), ('C', 'Y'), ('C', 'X'), ('C', 'R'), ('C', 'W'), ('C', 'V'), ('C', 'U'), ('S', 'Z'), ('S', 'Y'), ('S', 'X'), ('K', 'G'), ('K', 'E'), ('S', 'S'), ('S', 'R'), ('K', 'I'), ('K', 'H'), ('K', 'N'), ('K', 'M'), ('S', 'T'), ('S', 'K'), ('K', 'R'), ('S', 'I'), ('K', 'P'), ('K', 'W'), ('S', 'N'), ('S', 'M'), ('S', 'L'), ('S', 'C'), ('K', 'Z'), ('K', 'Y'), ('S', 'G'), ('S', 'E'), ('S', 'D'), ('D', 'O'), ('D', 'M'), ('D', 'J'), ('D', 'K'), ('V', 'G'), ('D', 'E'), ('Y', 'E'), ('D', 'Z'), ('U', 'S'), ('U', 'Y'), ('Y', 'T'), ('U', 'M'), ('L', 'B'), ('L', 'C'), ('L', 'A'), ('T', 'V'), ('T', 'W'), ('T', 'T'), ('T', 'R'), ('L', 'K'), ('L', 'I'), ('L', 'V'), ('T', 'O'), ('L', 'T'), ('L', 'U'), ('L', 'R'), ('L', 'S'), ('T', 'H'), ('T', 'F'), ('T', 'G'), ('T', 'D'), ('T', 'C'), ('L', 'Y'), ('V', 'A'), ('V', 'C'), ('A', 'E'), ('A', 'D'), ('A', 'G'), ('A', 'F'), ('A', 'I'), ('V', 'I'), ('I', 'S'), ('I', 'R'), ('A', 'M'), ('A', 'L'), ('A', 'O'), ('A', 'Q'), ('A', 'S'), ('A', 'R'), ('A', 'U'), ('A', 'T'), ('A', 'W'), ('I', 'N'), ('A', 'X'), ('A', 'Z'), ('I', 'E'), ('I', 'D'), ('U', 'A'), ('Q', 'A'), ('M', 'Z')], max_length=2, verbose_name='ISO Code'),
        ),
    ]
