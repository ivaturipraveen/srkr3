#include <iostream>
#include <vector>
#include <algorithm>

int main()
{
    std::vector<int> numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int target = 7;

    auto result = std::find(numbers.begin(), numbers.end(), target);

    if (result != numbers.end())
    {
        std::cout << "Element " << target << " found at position: " << std::distance(numbers.begin(), result) << std::endl;
    }
    else
    {
        std::cout << "Element " << target << " not found in the vector." << std::endl;
    }

    return 0;
}
