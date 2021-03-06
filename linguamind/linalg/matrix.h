#ifndef MATRIX_DEF
#define MATRIX_DEF

#include <vector>
#include <iostream>

#include "vector.h"
#include "seed.h"

class Matrix {

	public:
		Matrix(int rows, int cols);
		
		int destroy();
		
		int rows, cols;

		std::vector<Vector*> _data;

		Matrix zero();
		Matrix uniform(Seed* seed);
		void transpose();

		// std::vector<float> get();
		Vector* get(int i);
		// Vector* set(int i, Vector* x);
		void matmulset(Vector* input, Vector* output);
		void matmuladd(Vector* input, Vector* output);
		void Tmatmulset(Vector* input, Vector* output);
		void Tmatmuladd(Vector* input, Vector* output);

		void muli(float x);
		void subi(float x);

		Matrix operator*=(float x) const;
		Matrix operator/=(float x) const;
		Matrix operator+=(float x) const;
		Matrix operator-=(float x) const;

		Matrix operator*=(Matrix* x) const;
		Matrix operator/=(Matrix* x) const;
		Matrix operator+=(Matrix* x) const;
		Matrix operator-=(Matrix* x) const;
};

#endif

