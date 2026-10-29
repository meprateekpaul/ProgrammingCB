# Quiz 2 — Object-Oriented Programming & Data Visualisation
**Course:** Programming for Computational Biology (Python)  
**Covers:** Module 3 (OOP Pillars, Modifiers, ABC) & Module 4 (Matplotlib, Seaborn, Scientific Visualisation)  
**Time Allowed:** 45 minutes · **Total Marks:** 30

---

### Part A: Multiple Choice Questions (10 Marks, 1 Mark Each)

1. In Python, what occurs under the hood when an attribute name is prefixed with double underscores, such as `self.__private_id`?
   - A) Python's compiler locks the memory address against external writes.
   - B) Name mangling transforms the attribute name to `_ClassName__private_id`.
   - C) Python throws an immediate `PermissionError`.
   - D) It becomes a read-only CPython pointer.

2. Which decorator is used to define a read-only getter attribute in a biological class?
   - A) `@abstractmethod`
   - B) `@classmethod`
   - C) `@property`
   - D) `@staticmethod`

3. What happens if a subclass fails to implement an `@abstractmethod` defined in its parent class that inherits from `abc.ABC`?
   - A) Python raises a `TypeError` upon attempting to instantiate the subclass.
   - B) The missing method silently defaults to returning `None`.
   - C) A warning is printed to `sys.stderr` but execution continues.
   - D) The parent class constructor is skipped.

4. What is the Method Resolution Order (MRO) in Python?
   - A) The chronological order in which functions were defined in a module.
   - B) The algorithmic path (C3 linearization) Python uses to search for methods across class inheritance hierarchies.
   - C) The alphabetical sorting of class dunder methods.
   - D) A runtime optimizer for vectorised NumPy calls.

5. In Matplotlib's Object-Oriented interface, what do `fig` and `ax` represent in `fig, ax = plt.subplots()`?
   - A) `fig` is the global pyplot module; `ax` is the coordinate array.
   - B) `fig` is the top-level canvas container; `ax` is the individual plotting bounding box/coordinate system.
   - C) `fig` is a raster PNG; `ax` is an interactive widget.
   - D) They are identical interchangeable pointers.

6. Which plot type is most biologically appropriate for comparing the full multimodal distribution shape of gene expression across cell types?
   - A) Pie chart
   - B) Bar chart
   - C) Violin plot
   - D) Donut plot

7. In Seaborn, what parameter allows splitting and coloring data distributions by an experimental factor (e.g., wild-type vs knockout)?
   - A) `split_by`
   - B) `hue`
   - C) `palette_group`
   - D) `filter`

8. Why are 3D pie charts and rainbow (`jet`) colormaps discouraged in peer-reviewed scientific publications?
   - A) They consume too much memory during rendering.
   - B) 3D perspective distorts area proportions, and rainbow colormaps introduce false perceptual boundaries while failing colorblind accessibility standards.
   - C) Matplotlib has deprecated them in version 3.0.
   - D) They cannot be exported as vector PDF files.

9. What does the dunder method `__repr__` aim to return according to Python best practices?
   - A) An informal, pretty-printed string for casual user displays.
   - B) An unambiguous string representation that, if possible, looks like valid Python code to recreate the object.
   - C) An integer hash code for dictionary indexing.
   - D) A JSON-serialized byte stream.

10. Which command saves a high-resolution, publication-ready figure with tight bounding margins in Matplotlib?
    - A) `plt.export("figure.png", quality=100)`
    - B) `fig.savefig("figure.png", dpi=300, bbox_inches="tight")`
    - C) `ax.render(format="png", resolution="high")`
    - D) `plt.show(save=True)`

---

### Part B: Conceptual Short Answers (10 Marks, 2 Marks Each)

11. **Encapsulation vs Abstraction:** Explain the core technical difference between encapsulation and abstraction in the context of biological software design.

12. **Python's "Consenting Adults" Philosophy:** Why does Python not provide rigid, compiler-enforced `private` keywords like Java or C++?

13. **Seaborn Tidy Data Requirement:** What is meant by "tidy (long-form) data", and why does Seaborn prefer long-form DataFrames over wide matrices?

14. **Custom Annotations:** Write the exact Matplotlib command using `ax.annotate(...)` to draw an arrow pointing to a mutation site at coordinate `(175, 4.2)` with text `"R175H"`.

15. **Operator Overloading:** If you define `__add__(self, other)` on a `DNASequence` class, what biological behavior should `seq1 + seq2` exhibit?

---

### Part C: Code Design (10 Marks)

16. **(10 Marks)** Design a small OOP hierarchy:
    - Create an abstract class `BiologicalEntity(ABC)` with an abstract property `molecular_weight`.
    - Create a concrete subclass `NucleotideSequence(BiologicalEntity)` with attributes `identifier` (public), `_source` (protected), and `__sequence` (private).
    - Provide a `@property` for `sequence` (read-only) and implement `molecular_weight` returning `len(self.__sequence) * 330.0`.
    - Implement `__len__` returning the length of the sequence.
