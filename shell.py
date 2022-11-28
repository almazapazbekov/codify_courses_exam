from user.models import *
import datetime

python = Language(name='Python', month_to_learn=6)
python.save()
javascript = Language(name='Java Script ', month_to_learn=6)
javascript.save()
ux_ui_design = Language(name='UX-UI', month_to_learn=2)
ux_ui_design.save()

amanov_aman = Students(name='Amanov Aman', email='aman@mail.ru', phone_number='+996700989898',work_study_place='School №13', haw_own_notebook=True, preferred_os='windows')
amanov_aman.save()

apina_alena = Students(name='Apina Alena', email='aapina@bk.ru', phone_number='0550888888',work_study_place='TV', haw_own_notebook=True, preferred_os='mac')
apina_alena.save()

phil_spencer = Students(name='Phil Spencer', email='spencer@microsoft.com', phone_number='0508312312', work_study_place='Microsoft Gaming', haw_own_notebook=False, preferred_os='linux')
phil_spencer.save()

ilona_maskova = Mentor(name='Ilona Maskova', email='imask@gmail.com', phone_number='0500545454',main_work=None, experience=datetime.date(year=2021, month=10, day=23))
ilona_maskova.save()

halil_nurmuhametov = Mentor(name='Halil Nurmuhametov', email='halil@gmail.com', phone_number='0709989876', main_work='University of Fort Collins',experience=datetime.date(year=2010, month=9, day=18))
halil_nurmuhametov.save()

python21_1 = Course.objects.create(name='Python-21', mentor=halil_nurmuhametov, students=amanov_aman,date_started='2022-08-01', language=python)
python21_1.save()

python21_2 = Course.objects.create(name='Python-21', mentor=halil_nurmuhametov, students=apina_alena,date_started='2022-08-01', language=python)
python21_2.save()

ux_ui_43 = Course.objects.create(name='UXUI design-43', mentor=ilona_maskova, students=phil_spencer, date_started='2022-08-22', language=ux_ui_design)
ux_ui_43.save()
