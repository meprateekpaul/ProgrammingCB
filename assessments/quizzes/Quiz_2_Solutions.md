# Quiz 2 — Object-Oriented Programming & Data Visualisation (Answer Key & Solutions)
**Course:** Programming for Computational Biology (Python)  
**Covers:** Module 3 (OOP Pillars, Modifiers, ABC) & Module 4 (Matplotlib, Seaborn, Scientific Visualisation)  
**Total Marks:** 30

---

### Part A: Multiple Choice Questions (10 Marks, 1 Mark Each)

1. **Answer: B (`Name mangling transforms the attribute name to _ClassName__private_id.`)**  
   *Explanation:* Python performs identifier mangling at compile time, prepending `_ClassName` to prevent accidental name collisions across subclasses.

2. **Answer: C (`@property`)**  
   *Explanation:* `@property` creates a managed attribute descriptor exposing getter functionality without parentheses.

3. **Answer: A (`Python raises a TypeError upon attempting to instantiate the subclass.`)**  
   *Explanation:* Concrete subclasses must implement all abstract methods/properties; otherwise, Python prevents instantiation with `TypeError: Can't instantiate abstract class SubClass with abstract method...`.

4. **Answer: B (`The algorithmic path (C3 linearization) Python uses to search for methods across class inheritance hierarchies.`)**  
   *Explanation:* Method Resolution Order (MRO) uses the C3 supertree linearization algorithm to determine method lookup order in multiple inheritance.

5. **Answer: B (`fig is the top-level canvas container; ax is the individual plotting bounding box/coordinate system.`)**  
   *Explanation:* In Matplotlib OOP design, `Figure` represents the whole window/page/canvas, while `Axes` represents a coordinate area holding data points, ticks, spines, and labels.

6. **Answer: C (`Violin plot`)**  
   *Explanation:* Violin plots combine box plots with rotated kernel density estimates (KDE), showing multimodality and skewed distributions that box/bar plots obscure.

7. **Answer: B (`hue`)**  
   *Explanation:* The `hue` parameter in Seaborn groups data points by a categorical variable and maps them to distinguishable colors/palettes.

8. **Answer: B (`3D perspective distorts area proportions, and rainbow colormaps introduce false perceptual boundaries while failing colorblind accessibility standards.`)**  
   *Explanation:* Scientific visualization guidelines emphasize perceptually uniform sequential/diverging colormaps (e.g. viridis, magma) and un-distorted 2D geometry.

9. **Answer: B (`An unambiguous string representation that, if possible, looks like valid Python code to recreate the object.`)**  
   *Explanation:* Dunder `__repr__` targets developers and debuggers; by convention, `eval(repr(obj)) == obj` where practical.

10. **Answer: B (`fig.savefig("figure.png", dpi=300, bbox_inches="tight")`)**  
    *Explanation:* 300 DPI satisfies publication resolution standards, and `bbox_inches="tight"` crops extraneous whitespace around figure elements.

---

### Part B: Conceptual Short Answers (10 Marks, 2 Marks Each)

11. **Encapsulation vs Abstraction:**  
    *Answer:* **Encapsulation** bundles data state with methods and restricts direct outside tampering via access conventions (`_`, `__`, `@property`). **Abstraction** hides implementation complexity by exposing a high-level simplified interface (e.g., via abstract base classes like `abc.ABC`), so users interact with *what* the object does rather than *how* it does it.

12. **Python's "Consenting Adults" Philosophy:**  
    *Answer:* Python relies on convention rather than hard language fences (`"We are all consenting adults here"`). Instead of rigid private access specifiers, single underscores `_attr` signal protected internal state, trusting developers to respect architectural boundaries while keeping testing, debugging, and monkey-patching accessible.

13. **Seaborn Tidy Data Requirement:**  
    *Answer:* Tidy data requires each variable to form a column, each observation to form a row, and each observational unit to form a table. Seaborn leverages long-form tidy tables to easily map columns directly to aesthetic channels (`x`, `y`, `hue`, `col`, `row`).

14. **Custom Annotations:**  
    *Answer:*
    ```python
    ax.annotate(
        "R175H",
        xy=(175, 4.2),
        xytext=(185, 5.0),
        arrowprops=dict(facecolor="black", shrink=0.05, width=1, headwidth=6)
    )
    ```

15. **Operator Overloading:**  
    *Answer:* In a biological context, `seq1 + seq2` should model sequence concatenation (or ligation), returning a new `DNASequence` object whose nucleotide string is the concatenated sequence and whose length is `len(seq1) + len(seq2)`.

---

### Part C: Code Design (10 Marks)

16. **OOP Hierarchy Implementation:**
```python
from abc import ABC, abstractmethod

class BiologicalEntity(ABC):
    """Abstract base class for all biological entities."""
    @property
    @abstractmethod
    def molecular_weight(self) -> float:
        """Return the molecular weight in Daltons."""
        pass


class NucleotideSequence(BiologicalEntity):
    """Represents a nucleotide sequence with encapsulated sequence data."""
    def __init__(self, identifier: str, sequence: str, source: str = "GenBank"):
        self.identifier = identifier        # Public attribute
        self._source = source              # Protected attribute
        self.__sequence = sequence.upper() # Private attribute (name-mangled)

    @property
    def sequence(self) -> str:
        """Read-only property returning the nucleotide sequence."""
        return self.__sequence

    @property
    def molecular_weight(self) -> float:
        """Estimated molecular weight (approx 330 Da per nucleotide)."""
        return len(self.__sequence) * 330.0

    def __len__(self) -> int:
        return len(self.__sequence)
```
