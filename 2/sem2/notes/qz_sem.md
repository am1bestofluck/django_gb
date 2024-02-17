как работает рандом в дефолтных значениях моделей	генерируется 1 раз, потом присваивается
* как перезаполнять UPDATE-поля экземлляров, и почему(try/if)	через if kwargs['field_name'], потому что try ложит в поле null
* импортируем lorem   from django.utils import lorem_ipsum
* Как создаём новую запись в ManyToManyField	сначала создаём объект, потом MtM заполняем через for itm in MtM_itms: Model_name.MtM_field.add(itm)
* оверврайтим метод save у модели 	def save(* args,** kwargs); делаем что хотим с полями, которые уже объявлены; super(ModelName,self).save(* args, ** kwargs)
* нативный консольный интерфейс django для консоли 	argparse
* собираем позиционные аргументы в список nargs="+"/" * "
* в чём разница между nargs='+' и nargs=' * ' 	+ принимает выдаст ошибку если не переданы аргументы
* как передать позиционный агрумент в модель 	class Command(BaseCommand):  def add_arguments(self,parser):  parser.add_argument("arg_name",type=int)
* как передать ключевой/опциональный агрумент в модель 	class Command(BaseCommand):  def add_arguments(self,parser):  parser.add_argument("--arg_name",type=int)
* как задавать опциональным аргументам значение по умолчанию(булево) 	def add_arguments(self,parser): parser.add_argument( "--optional_key_only",
 action="store_true"|"store_false")
* вывод в консоль из кастомных команд self.stdout|stderr.write("only_strings")
* что передавать в self.stdout.write() 	строки
