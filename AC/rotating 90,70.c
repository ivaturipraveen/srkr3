#include <stdio.h>

void printMatrix(int mat[3][3])
{
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            printf("%d\t", mat[i][j]);
        }
        printf("\n");
    }
}

void rotateClockwise270(int a[3][3], int b[3][3])
{
    for (int i = 0, l = 0; i < 3; i++, l = 0)
    {
        for (int j = 2, k = 0; j >= 0; j--, k++)
        {
            b[i][k] = a[i][j];
        }
    }
}

void rotateAntiClockwise90(int a[3][3], int b[3][3])
{
    for (int i = 0, l = 0; i < 3; i++, l = 0)
    {
        for (int j = 0, k = 2; j < 3; j++, k--)
        {
            b[i][k] = a[i][j];
        }
    }
}

int main()
{
    int a[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int b[3][3];

    printf("Original Matrix:\n");
    printMatrix(a);

    // Rotate clockwise by 270 degrees
    rotateClockwise270(a, b);
    printf("\nMatrix after rotating clockwise by 270 degrees:\n");
    printMatrix(b);

    // Reset matrix for the next rotation
    int c[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};

    // Rotate anticlockwise by 90 degrees
    rotateAntiClockwise90(c, b);
    printf("\nMatrix after rotating anticlockwise by 90 degrees:\n");
    printMatrix(b);

    return 0;
}
