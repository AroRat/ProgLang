#include <iostream>

namespace Flow
{
    void er()
    {
        std::cout << "Imagine there is rose." << std::endl;
    }
}

namespace Powd
{
    void er()
    {
        std::cout << "Imagine there is... no, don't do it." << std::endl;
    }
}

int main()
{
    Flow::er();
    Powd::er();
}