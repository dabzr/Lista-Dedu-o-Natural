---
title: Deduction
marimo-version: 0.11.6
width: medium
---

```python {.marimo}
from nadia.nadia_pt_fo import check_proof
```

```python {.marimo}
import marimo as mo
```

## Lista de Dedução Natural
<!---->
Questão 1

∀xP(x) ∨ Q(y) ⊢ ∀x(P(x) ∨ Q(y))

```python {.marimo hide_code="true"}
q1 = """
1. AxP(x) | Q(y)     pre
2. { a
3.    { AxP(x)       hip
4.      P(a)         Ae 3
5.      P(a) | Q(y)  |i 4
      }
6.    { Q(y)         hip
7.      P(a) | Q(y)  |i 6
      }
8. P(a) | Q(y)       |e 1, 3-5, 6-7
}
9. Ax(P(x) | Q(y)) Ai 2-8
"""
mo.show_code()
```

```python {.marimo hide_code="true"}
mo.md(check_proof(q1, display_fitch=False, display_gentzen=False))
```

Questão 2

∀x(P(x) ∨ Q(y)) ⊢ ∀xP(x) ∨ Q(y)

```python {.marimo hide_code="true"}
q2 = """
1. Ax(P(x) | Q(y))     pre
2. { ~(AxP(x) | Q(y))  hip
3.   { Q(y)            hip
4.     AxP(x) | Q(y)   |i 3
5.     @               ~e 2, 4
     }
6.   ~Q(y)             ~i 3-5
7.   { a
8.     P(a) | Q(y)     Ae 1
9.     {P(a)           hip}
10.    { Q(y)          hip
11.     @              ~e 6, 10
12.     P(a)           @e 11
       }
13.    P(a)            |e 8, 9-9, 10-12
     }
14.  AxP(x)            Ai 7-13
15.  AxP(x) | Q(y)     |i 14
16.  @                 ~e 2, 15
   }
17. AxP(x) | Q(y)      raa 2-16
"""
mo.show_code()
```

```python {.marimo hide_code="true"}
mo.md(check_proof(q2, display_fitch=False, display_gentzen=False))
```

Questão 3

∃xP(x) ∨ ∃xQ(x) ⊢ ∃x(P(x) ∨ Q(x))

```python {.marimo hide_code="true"}
q3 = """
1. ExP(x) | ExQ(x)     pre
2. { ExP(x)            hip
3.   { a P(a)          hip
4.     P(a) | Q(a)     |i 3
5.     Ex(P(x) | Q(x)) Ei 4
     }
6.   Ex(P(x) | Q(x))   Ee 2, 3-5
   }
7. { ExQ(x)            hip
8.   {a Q(a)           hip
9.    P(a) | Q(a)      |i 8
10.   Ex(P(x) | Q(x))  Ei 9
     }
11.  Ex(P(x) | Q(x))   Ee 7, 8-10
   }
12. Ex(P(x) | Q(x))    |e 1, 2-6, 7-11
"""
mo.show_code()
```

```python {.marimo hide_code="true"}
mo.md(check_proof(q3, display_fitch=False, display_gentzen=False))
```

Questão 4

∃x(P(x) ∨ Q(x)) ⊢ ∃xP(x) ∨ ∃xQ(x)

```python {.marimo hide_code="true"}
q4 = """
1. Ex(P(x) | Q(x))      pre
2. { a P(a) | Q(a)      hip
3.   {P(a)              hip
4.    ExP(x)            Ei 3
5.    ExP(x) | ExQ(x)   |i 4
     }
6.   {Q(a)              hip
7.    ExQ(x)            Ei 6
8.    ExP(x) | ExQ(x)   |i 7
     }
9.   ExP(x) | ExQ(x)    |e 2, 3-5, 6-8
  }
10. ExP(x) | ExQ(x)     Ee 1, 2-9
"""
mo.show_code()
```

```python {.marimo hide_code="true"}
mo.md(check_proof(q4, display_fitch=False, display_gentzen=False))
```