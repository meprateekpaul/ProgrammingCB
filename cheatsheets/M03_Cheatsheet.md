# Module 3 Cheatsheet — Object-Oriented Programming (OOP)

### Class Skeleton & Dunder Methods
```python
class DNASequence:
    # Class attribute shared by all instances
    ALPHABET = set("ACGT")

    def __init__(self, identifier: str, sequence: str):
        self.identifier = identifier
        self._sequence = sequence.upper()  # Protected
        self.__cached_gc = None            # Private

    def __len__(self):
        return len(self._sequence)

    def __str__(self):
        return f">{self.identifier}\n{self._sequence[:30]}..."

    def __repr__(self):
        return f"DNASequence(identifier={self.identifier!r}, sequence={self._sequence!r})"

    def __add__(self, other):
        if isinstance(other, DNASequence):
            return DNASequence(f"{self.identifier}+{other.identifier}", self._sequence + other._sequence)
        raise TypeError("Cannot concatenate non-DNASequence")

    @property
    def gc_content(self) -> float:
        if self.__cached_gc is None:
            g = self._sequence.count("G")
            c = self._sequence.count("C")
            self.__cached_gc = (g + c) / len(self._sequence) * 100
        return self.__cached_gc

    @classmethod
    def from_fasta(cls, path):
        # Alternate constructor
        ...
```

### Access Modifiers in Python
| Modifier | Syntax | Scope | Note |
|---|---|---|---|
| **Public** | `self.id` | Everywhere | Standard attribute |
| **Protected** | `self._id` | Class & subclasses | Convention only |
| **Private** | `self.__id` | Class only | Name-mangled to `_Class__id` |

### Abstraction with `abc.ABC`
```python
from abc import ABC, abstractmethod

class BiologicalSequence(ABC):
    @property
    @abstractmethod
    def alphabet(self) -> set:
        pass

    @abstractmethod
    def molecular_weight(self) -> float:
        pass

class DNA(BiologicalSequence):
    @property
    def alphabet(self):
        return set("ACGT")

    def molecular_weight(self):
        return len(self.seq) * 330.0
```
