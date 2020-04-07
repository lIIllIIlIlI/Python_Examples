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



Singleton:

Die Singleton class ist eine Implementierung der Meta class.



Decorators:

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

