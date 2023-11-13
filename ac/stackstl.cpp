#include <iostream>
#include <stack>

int main()
{
    std::stack<int> myStack;

    // Push elements onto the stack
    myStack.push(1);
    myStack.push(2);
    myStack.push(3);

    // Print the top element of the stack
    std::cout << "Top element of the stack: " << myStack.top() << std::endl;

    // Pop elements from the stack
    myStack.pop();

    // Check if the stack is empty
    if (myStack.empty())
    {
        std::cout << "Stack is empty." << std::endl;
    }
    else
    {
        std::cout << "Stack is not empty." << std::endl;
    }

    return 0;
}
