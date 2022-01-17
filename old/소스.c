#include <stdio.h>
#include <math.h>
#define PI  3.141592654


void createTMatrix(int jointNo, double param[3][4], double T[4][4]);
void multTransform(double A[4][4], double B[4][4], double C[4][4]);
void print4x4Mtx(char *str, double A[4][4]);

int main(void)
{
	double T_0_1[4][4];			// Homogeneous Transform Matrix from {0} to {1}
	double T_1_2[4][4];			// Homogeneous Transform Matrix from {1} to {2}
	double T_2_3[4][4];			// Homogeneous Transform Matrix from {2} to {3}
	double T_0_3[4][4];         // �κ� ���̽� {0} ���� {3} �� ǥ���ϴ� ���
	double T_0_2[4][4];
	double param[3][4] = { 0, };	// �׸� 3.8 �� ��ũ���� ���
	double L1 = 1.0;			// L1 = 1 ����
	double L2 = 1.0;			// L2 = 1 ����
	int i, jointNo;
	double theta;			// ����ڿ��Լ� �Է� ���� ���� ��

	//**** �Ķ���� ��� �ʱ�ȭ.�׸� 3.8
	param[1][1] = L1;
	param[2][1] = L2;

	//**** ����ڿ��Լ� ���� �� 3���� �Է� �޾Ƽ� param ��Ŀ� ����Ѵ�. 
	for (i = 0; i < 3; i++) {
		printf("���� %d �� ���� �Է��ϼ���(����: ��) : ", i + 1);
		scanf_s("%f", &theta);
		param[i][3] = theta * PI / 180.0;		// degree �� radian ���� ��ȯ
	}

	//**** ��ȯ ��� ���
	jointNo = 0;						// 1 �� ����
	createTMatrix(jointNo, param, T_0_1);		// ��ȯ��� ���
	// [�ڵ�] T_0_1 ��� ȭ�鿡 ����ϰ� ����.
	print4x4Mtx("T_0_1", T_0_1);

	jointNo = 1;						// 2 �� ����
	createTMatrix(jointNo, param, T_1_2);		// ��ȯ��� ���
	// [�ڵ�] T_1_2 ��� ȭ�鿡 ����ϰ� ����.
	print4x4Mtx("T_1_2", T_1_2);

	jointNo = 2;						// 3 �� ����
	createTMatrix(jointNo, param, T_2_3);		// ��ȯ��� ���
	// [�ڵ�] T_2_3 ��� ȭ�鿡 ����ϰ� ����.
	print4x4Mtx("T_2_3", T_2_3);

	//**** ��ȯ��� �����Ͽ� T_0_3 ���
	multTransform(T_0_1, T_1_2, T_0_2);
	multTransform(T_0_2, T_2_3, T_0_3);	// T_0_3 ���
	// [�ڵ�] T_0_3 ��� ȭ�鿡 ����ϰ� ����.
	print4x4Mtx("T_0_3", T_0_3);

	//[�ڵ�]���� ������ �̿��ؼ� �κ��� ��ũ ��ġ�� �׸����� �׸��� �Ѵ�. 
	// �κ� ��ǥ�� {1}, {2}, {3} �� ���� (x,y) ��ǥ�� ���Ͽ� ����Ѵ�. 
	// ���Ŀ� ������ ��� �κ��� ��ũ ��ġ�� �׸����� �׷��� ��ġ�� Ȯ���Ѵ�. 
	printf("X2,Y2 = ( %f , %f )", T_0_2[0][3], T_0_2[1][3]);
	printf("X3,Y3 = ( %f , %f )", T_0_3[0][3], T_0_3[1][3]);

	return 0;
}

void createTMatrix(int jointNo, double param[3][4], double T[4][4])
{
	// �Է�
	//		int jointNo        : ���� ��ȣ. 0,1,2
	//		double param[3][4] : �Ķ���� ���
	// ��ȯ
	//		double T[4][4]     : ���� ��ȯ���. �� (3.6) �� ����Ͽ� ��ȯ�Ѵ�. 
	//

	double alpha_i_1, a_i_1, d_i, theta_i;

	alpha_i_1 = param[jointNo][0];
	a_i_1 = param[jointNo][1];
	d_i = param[jointNo][2];
	theta_i = param[jointNo][3];

	//[�ڵ�]  �� (3.6)�� ���⿡ �ڵ�.
	T[0][0] = cos(theta_i);
	T[0][1] = -sin(theta_i);
	T[0][2] = 0.0;
	T[0][3] = alpha_i_1;
	T[1][0] = sin(theta_i)*cos(alpha_i_1);
	T[1][1] = cos(theta_i)*cos(alpha_i_1);
	T[1][2] = -sin(alpha_i_1);
	T[1][3] = -sin(alpha_i_1)*d_i;
	T[2][0] = sin(theta_i)*sin(alpha_i_1);
	T[2][1] = cos(theta_i)*sin(alpha_i_1);
	T[2][2] = cos(alpha_i_1);
	T[2][3] = cos(alpha_i_1)*d_i;
	T[3][0] = 0.0;
	T[3][1] = 0.0;
	T[3][2] = 0.0;
	T[3][3] = 1.0;



}

void multTransform(double A[4][4], double B[4][4], double C[4][4])
{
	// �Է� :  �ΰ��� ��ȯ ��� A[4][4],  B[4][4]
	//
	// ��ȯ :  C ��� = A * B

	//[�ڵ�] �� ����� ������ ���� �ڵ�
	int x = 0, j = 0, k = 0;
	for (x = 0; x < 4; x++) {
		for (j = 0; j < 4; j++) {
			for (k = 0; k < 4; k++)
				C[x][j] = A[x][k] * B[k][j];
		}
	}

}

void print4x4Mtx(char *str, double C[4][4])
{
	int x = 0, j = 0;
	for (x = 0; x < 4; x++) {
		for (j = 0; j < 4; j++) {
			printf("%2f  ", C[x][j]);
		}
		putchar('\n');
	}
}