
#include <iostream>
#include <vector>
#include <chrono>

int main() {
    auto start = std::chrono::high_resolution_clock::now(); // Start the timer
    std::vector<int> values;
    for (int i = 0; i < 100000; ++i) {
        values.push_back(i * i);
    }
    auto end = std::chrono::high_resolution_clock::now(); // End the timer
    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
    std::cout << "Elapsed time: " << duration.count() << " microseconds" << std::endl;
    return 0;
}