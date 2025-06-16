# Challenge #17: Sorting on a Systolic Array

## 🔹 Overview

This challenge focuses on implementing **Bubble Sort** using a **systolic array architecture**, simulating the design in software, and analyzing its performance.

---

## 📚 Learning Goals

- Understand Bubble Sort implementation on a systolic array.
- Design the systolic array dimension needed for sorting.
- Simulate and test the systolic Bubble Sort algorithm.
- Measure and visualize execution times for various input sizes.

---

## 🔹 Systolic Array Design

- **Architecture:** Linear array of `N-1` processing elements (PEs) for sorting `N` elements.
- **Operation:** Each PE compares and swaps adjacent elements per clock cycle.
- **Execution:** Requires approximately `N` passes, resulting in O(N²) time complexity.

---

## 🔹 Performance Visualization

Measured execution times for input sizes: 10, 100, 1000, 3000.  
Observed quadratic growth in runtime consistent with Bubble Sort complexity.

Sample plot generated using `matplotlib` to visualize execution time vs input size.

---

## 🔹 What We Observe

- Execution time grows approximately **quadratically (O(N²))** with input size.
- The systolic array’s linear structure aligns naturally with Bubble Sort’s compare-and-swap steps.
- Bubble Sort’s inefficiency for large datasets is evident, highlighting the need for more efficient sorting algorithms for scaling.

---

## 🔹 Conclusion

- The systolic array for Bubble Sort requires `N-1` PEs to handle `N` elements.
- Software simulation provides insight into systolic data movement and timing.
- This challenge reinforces understanding of algorithm-hardware mapping and performance implications.

---