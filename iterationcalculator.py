import sympy as sp
import mpmath

def main():
    # Benutzer gibt die Funktion ein
    funktion = input("Gib eine Funktion ein (z.B. '2*x*21 - 3*x**2'): ")

    # Parse der Funktion
    x = sp.symbols('x')
    term = sp.sympify(funktion)

    # Ableitung der Funktion
    derivative = sp.diff(term, x)
    max_order = 6  # Maximale Ableitungsordnung

    print(f"Funktion: {funktion}")

    # Iteration, um Ableitungen zu berechnen, bis die Funktion den Wert 0 erreicht
    x_value = 1.0  # Startpunkt für die Iteration
    iteration = 1

    while iteration <= max_order:
        # Überprüfung, ob die Ableitung an der aktuellen Iterationsstelle nicht null ist
        result_value = derivative.subs(x, x_value)
        if abs(result_value) < 1e-15:
            print(f"Iteration {iteration}: {derivative} hat den Wert 0 erreicht bei x = {x_value}")
            break

        print(f"Iteration {iteration}: {derivative}")

        # Berechnung der nächsten Iteration
        derivative = sp.diff(derivative, x)
        
        # Überprüfung auf Division durch Null
        if derivative == 0:
            print("Division durch Null vermieden. Breche ab.")
            break

        x_value -= mpmath.mp.re(result_value) / mpmath.mp.re(derivative.subs(x, x_value))

        iteration += 1

    # Zusätzliche Iteration, um die gewünschte Iteration 5 zu erhalten
    if iteration == 5:
        result_value = derivative.subs(x, x_value)
        print(f"Iteration {iteration}: {result_value} hat den Wert 0 erreicht bei x = {x_value}")

if __name__ == "__main__":
    main()

