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
	double T_0_3[4][4];         // 로봇 베이스 {0} 에서 {3} 을 표현하는 행렬
	double T_0_2[4][4];
	double param[3][4] = { 0, };	// 그림 3.8 의 링크인자 행렬
	double L1 = 1.0;			// L1 = 1 미터
	double L2 = 1.0;			// L2 = 1 미터
	int i, jointNo;
	double theta;			// 사용자에게서 입력 받을 관절 각

	//**** 파라미터 행렬 초기화.그림 3.8
	param[1][1] = L1;
	param[2][1] = L2;

	//**** 사용자에게서 관절 각 3개를 입력 받아서 param 행렬에 기록한다. 
	for (i = 0; i < 3; i++) {
		printf("관절 %d 의 각을 입력하세요(단위: 도) : ", i + 1);
		scanf_s("%f", &theta);
		param[i][3] = theta * PI / 180.0;		// degree 를 radian 으로 변환
	}

	//**** 변환 행렬 계산
	jointNo = 0;						// 1 번 관절
	createTMatrix(jointNo, param, T_0_1);		// 변환행렬 계산
	// [코딩] T_0_1 행렬 화면에 출력하고 관찰.
	print4x4Mtx("T_0_1", T_0_1);

	jointNo = 1;						// 2 번 관절
	createTMatrix(jointNo, param, T_1_2);		// 변환행렬 계산
	// [코딩] T_1_2 행렬 화면에 출력하고 관찰.
	print4x4Mtx("T_1_2", T_1_2);

	jointNo = 2;						// 3 번 관절
	createTMatrix(jointNo, param, T_2_3);		// 변환행렬 계산
	// [코딩] T_2_3 행렬 화면에 출력하고 관찰.
	print4x4Mtx("T_2_3", T_2_3);

	//**** 변환행렬 곱셈하여 T_0_3 계산
	multTransform(T_0_1, T_1_2, T_0_2);
	multTransform(T_0_2, T_2_3, T_0_3);	// T_0_3 계산
	// [코딩] T_0_3 행렬 화면에 출력하고 관찰.
	print4x4Mtx("T_0_3", T_0_3);

	//[코딩]엑셀 파일을 이용해서 로봇의 링크 위치를 그림으로 그리려 한다. 
	// 로봇 좌표계 {1}, {2}, {3} 의 원점 (x,y) 좌표를 파일에 기록한다. 
	// 이후에 엑셀로 열어서 로봇의 링크 위치를 그림으로 그려서 위치를 확인한다. 
	printf("X2,Y2 = ( %f , %f )", T_0_2[0][3], T_0_2[1][3]);
	printf("X3,Y3 = ( %f , %f )", T_0_3[0][3], T_0_3[1][3]);

	return 0;
}

void createTMatrix(int jointNo, double param[3][4], double T[4][4])
{
	// 입력
	//		int jointNo        : 관절 번호. 0,1,2
	//		double param[3][4] : 파라미터 행렬
	// 반환
	//		double T[4][4]     : 계산된 변환행렬. 식 (3.6) 을 계산하여 반환한다. 
	//

	double alpha_i_1, a_i_1, d_i, theta_i;

	alpha_i_1 = param[jointNo][0];
	a_i_1 = param[jointNo][1];
	d_i = param[jointNo][2];
	theta_i = param[jointNo][3];

	//[코딩]  식 (3.6)을 여기에 코딩.
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
	// 입력 :  두개의 변환 행렬 A[4][4],  B[4][4]
	//
	// 반환 :  C 행렬 = A * B

	//[코딩] 두 행렬의 곱셉을 여기 코딩
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