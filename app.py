import streamlit as st
import numpy as np


def multiply_matrices(matrix1, matrix2):
    result = np.dot(matrix1, matrix2)
    return result

def main():
    st.title("Perkalian Matriks 2x2")
    
    # Input matriks pertama
    st.subheader("Matriks Pertama")
    matrix1 = []
    for i in range(2):
        row = []
        for j in range(2):
            value = st.number_input(f"Masukkan nilai matriks1[{i+1}][{j+1}]", key=f"matrix1_{i}_{j}")
            row.append(value)
        matrix1.append(row)
    
    # Input matriks kedua
    st.subheader("Matriks Kedua")
    matrix2 = []
    for i in range(2):
        row = []
        for j in range(2):
            value = st.number_input(f"Masukkan nilai matriks2[{i+1}][{j+1}]", key=f"matrix2_{i}_{j}")
            row.append(value)
        matrix2.append(row)
    
    # Tombol hitung
    if st.button("Hitung"):
        result = multiply_matrices(matrix1, matrix2)
        st.subheader("Hasil Perkalian")
        st.write(result)

if __name__ == "__main__":
    main()


def determinant_2x2(matrix):
    det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    return det

def main():
    st.title("Determinan Matriks 2x2")
    st.write("Masukkan nilai elemen matriks 2x2:")

    matrix = []
    for i in range(2):
        row = []
        for j in range(2):
            value = st.number_input(f"Masukkan elemen matriks [{i}][{j}]:", key=f"matrix[{i}][{j}]")
            row.append(value)
        matrix.append(row)

    if st.button("Hitung Determinan"):
        det = determinant_2x2(matrix)
        st.success(f"Determinan matriks: {det}")

if __name__ == "__main__":
    main()


def inverse_matrix(matrix):
    det = matrix[0, 0] * matrix[1, 1] - matrix[0, 1] * matrix[1, 0]
    if det == 0:
        return None
    else:
        inv_matrix = np.zeros_like(matrix)
        inv_matrix[0, 0] = matrix[1, 1] / det
        inv_matrix[0, 1] = -matrix[0, 1] / det
        inv_matrix[1, 0] = -matrix[1, 0] / det
        inv_matrix[1, 1] = matrix[0, 0] / det
        return inv_matrix

def main():
    st.title("Invers Matriks 2x2")
    
    st.write("Masukkan elemen-elemen matriks:")
    a = st.number_input("A[0, 0]", value=0.0)
    b = st.number_input("A[0, 1]", value=0.0)
    c = st.number_input("A[1, 0]", value=0.0)
    d = st.number_input("A[1, 1]", value=0.0)
    
    matrix = np.array([[a, b], [c, d]])
    
    if st.button("Hitung Invers"):
        inv_matrix = inverse_matrix(matrix)
        if inv_matrix is None:
            st.error("Determinan matriks adalah 0. Matriks tidak dapat diinvers.")
        else:
            st.success("Invers matriks:")
            st.write(inv_matrix)
            

if __name__ == "__main__":
    main()
