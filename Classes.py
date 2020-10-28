__new__ vs __init__:

new wird in Metaklassen verwendet um zu bestimmen, wie ein Object der Klasse kreiert wird. Init wird aufgerufen, um eine Instanz der Klasse zu initialisieren.

Super:

Is used to access inherited functions. Super is called by "super().methodname(args)" which is a shortcut for "super(subClass, instance).method(args)". Example:

class parentClass(object):

    def __init__(self):

          pass

class childClass(parentClass):

    def __init__(self):

old python:

           super(childClass, self).__init__()

python >3.0 master race:

           super().__init__()

Super in this case, will always call the class the child is inheriting from. So in case the upper class gets exchanged,

the super function automatically calls the newer function. This make the code much more portable, especially in

large class structures.


Meta class:

    Eine Metaklasse definiert das verhalten einer Klasse. Eine Klasse instanziiert Objekte, eine Metaklasse instanziiert Klassen und erlaubt die erstellung zu customizen.
    Klassen sind ihrerseits nur Objects, Python interpretiert das keyword und gibt ein Object zurück. Dieses Objekt hat die besondere eigenschaften, selbst objekte (Instanzen) erzeugen zu können. Statt class myClass() könnte man auch type(name, bases, attrs) aufrufen: type('myClass', (),  {}). Bases ist ein Tuple auf prent classes. Daher können Klassen wie alle anderen Objekte zwischen Klassen ausgetauscht und im Programmcode verwendet werden. Attrs definiert innerhalb des Klassen namespaces definierter Variablen, e.h.
               class myClass():                           vs    myClass = type('myClass', (), {'myVariable': True})
                         myVariable = True
    Selbst Funktionen können so übergeben werden, indem sie definiert werden und anschließend in die attrs eingetragen werden.
    Python verwendet die Metaklasse 'type' als default zum erstellen von Klassen Objekten. Nun ist es möglich, seine eigene Metaklasse zu hinterlegen um diese stattdess aufrufen zu lassen.
    Um eine Metaklasse einzusetzen muss eine Funktion mit gleichen Parametern geschrieben werden und entweder modulweit (__metaclass__ = myFunction) oder class myFunction(__metaclass__=myFunctioN) deklariert werden. Innerhalb der Funktion kann man die Parameter beliebig umbiegen um anschließend per type das object zu erstellen und zurück zu liefern.
    Die hinterlegte Metaklasse kann auch eine Funktion sein, als "best practice" sollte sie das jedoch sein.
    Datenklassen sind dark magic und nur in wenigen Spezialfällen notwendig
    Die meisten Probleme lassen sich statt mit Metaklassen besser mit decorators oder monkey patching lösen.


Abstract class:

    Die abstrakte klasse ist eine Implementierung der Meta class.
    Sie kann nicht instanziiert werden.
    Alle Kinder der Klasse müssen alle definierten Methoden implementieren#
    Die Methoden der Abstrakten Klasse können über das super Keyword angesprochen werden

    from abc import ABC
    from abc import abstractmethod

    class abstractClass(ABC):
        def __init__(self):
            print("Hello ")
            return
     @abstractmethod
        def printer(self):
            print("im printer")
            return

    class derivedClass(abstractClass):

        def __init__(self):
            super().__init__()
            print("World!")
            return

        def printer(self):
            print("Hello world, ")
            super().printer()
            return

Singleton:

    Singletons sind unter Python nativ nicht verfügbar. Es gibt mehrer Lösungen, das Konstrukt nachzubauen. Die Pythonic Lösung dafür ist die Verwendung von metaclasses.
    class Singleton(type):

        _instances = {}
        def __call__(cls, *args, **kwargs):
            if cls not in cls._instances:
                cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
            return cls._instances[cls]

    class MyClass(BaseClass, metaclass=Singleton):
        pass


Decorators

    Ein decorator ist die Light Version einer Metaklasse. Er erhält das Objekt eines bestimmten Types, modelliert es und gibt es anschließend wieder zurück.
    Im Falle einer Funktion wird eine Funktion in den Decorator reingegeben und eine zurückgegeben, er agiert also als Wrapper.  

    def make_pretty(func):
        def inner():
            print("I got decorated")
            func()
        return inner

    def ordinary():
        print("I am ordinary")
    ordinary = makepretty(ordinary)

    Python bietet hierfür eine verkürzte Schreibweise um eine Funktion vom Decorator "wrappen" zu lassen
    @make_pretty
    def ordinary():
        print("I am ordinary")

    Es können mehrere @ decorators hintereinander aufgeführt werden, die Funktion wird hintereinander durch alle durchgepipt.

    Das ganze funktioniert nicht nur mit Funktionen, sondern auch mit Klassen und stellt häufig eine deutliche einfachere Alternative zu Metaklassen dar

Dataclasses

    Datenklassen werden verwendet, um Initialisierungcode zu sparen. Wenn eine Klasse während der Initialisierung eine lange liste von Variablen einfach nur zuweist und sie nicht weiter verarbeitet, dann kann die Datenklasse diesen Job automatisieren. Die Initi Funktion wird automatisch eingefügt und definiert die Membervariablen hintereinander weg. Das Funktioniert nur solange die init ansonsten keine Funktionalität erfüllt.

    @dataclass
    class InventoryItem:
        '''Class for keeping track of an item in inventory.'''
        name: str
        unit_price: float
        quantity_on_hand: int = 0

        def total_cost(self) -> float:
            return self.unit_price * self.quantity_on_hand

Property

    Abstrahiert setter und getter. Wird anschließend auf die besagt variable zugegriffen, wird python automatisch den dafür vorgesehenen Getter oder Setter aufrufen.Beachte: Die Temerpatur wird als private deklariert, von außen aber direkt als "object.temperatur" statt "object._temperatur" angesprochen. Das gleiche gilt für Methoden der Klasse, hier "to_fahrenheit".

    class Celsius:
        def __init__(self, temperature = 0):
            self._temperature = temperature

        def to_fahrenheit(self):
            return (self.temperature * 1.8) + 32

        @property
        def temperature(self):
            print("Getting value")
            return self._temperature

        @temperature.setter
        def temperature(self, value):
            if value < -273:
                raise ValueError("Temperature below -273 is not possible")
            print("Setting value")
            self._temperature = value

class A:
  """
  some random class
  """
  def __init__(self, name, myString):
    self.name = name
    self.myString = myString
    self.anotherVar = 5

  def __str__(self):
    """
    This one should give the user a quick feedback
    """
    objectDescriptionString = "\n"
    objectDescriptionString += " name: " + str(self.name) + ",\n"
    objectDescriptionString += " myString: " + str(self.myString) + ",\n"
    objectDescriptionString += " anotherVar: " + str(self.anotherVar) + ">\n"
    return objectDescriptionString
    
  def __repr__(self):
      """
      There is a implicit default __repr__ that prints "self.__class__.__name__, id(self)". This defines what is returned 
      when print is called on the function. To create a pretty printing, this can be explicitely overriden.
      __repr__ should give some information about the object to developer.
      """
      objectDescriptionString = "\n"
      objectDescriptionString += "<class: " + self.__class__.__name__ + ",\n"
      objectDescriptionString += " name: " + str(self.name) + ",\n"
      return objectDescriptionString
      
myObject = A("greeting", "hello world") 
print(myObject)
