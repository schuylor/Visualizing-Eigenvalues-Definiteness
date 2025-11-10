## Visualizing Eigenvalues & Definiteness
*A geometric playground for quadratic forms, curvature, and matrix definiteness.*

Given a symmetric matrix \(A \in \mathbb{R}^{2 \times 2}\), this project visualizes the quadratic form

\[
x^\top A x
\]

and plots the surface

\[
z = x^\top A x.
\]

This helps us *see* eigenvalues and definiteness, not just memorize them.

---

## Why visualize eigenvalues?

For any non-zero vector \(x\),

\[
x^\top A x \ge 0
\]

means the matrix is **Positive Semi-Definite (PSD)**.  
If all eigenvalues \(>0\), the matrix is **Positive Definite (PD)**.

Eigenvalues describe **curvature**:

| Matrix Type | Eigenvalues | Geometry |
Positive Definite (PD) | all \(>0\) | Convex bowl |
Positive Semi-Definite (PSD) | \(\ge 0\) and some \(=0\) | Bowl with flat directions |
Negative Definite (ND) | all \(<0\) | Upside-down bowl |
Indefinite | mixed signs | Saddle |

So eigenvalues = *principal curvature directions*.  
This matters because it connects to:

- Optimization & convexity  
- Hessians in ML  
- Why \(X^\top X\) in regression is PSD  
- Why ridge regression adds \(\lambda I\) to lift eigenvalues  

Instead of treating it as algebra, we treat it as **geometry**.

