#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> floodFill(std::vector<std::vector<int>>& image, int sr, int sc, int newColor) {
        rows_ = image.size();
        cols_ = image[0].size();
        newColor_ = newColor;
        replaced_ = image[sr][sc];
        if (replaced_ == newColor) return image;

        image[sr][sc] = newColor_;
        solve(image, sr, sc);
        return image;
    }

    void solve(std::vector<std::vector<int>>& image, int x, int y) {
        std::vector<std::vector<int>> directions{{0, -1}, {-1, 0}, {0, 1}, {1, 0}};
        int dx, dy;
        for (auto dir : directions) {
            dx = x + dir[0];
            dy = y + dir[1];
            if (dx < 0 || dx >= rows_ || dy < 0 || dy >= cols_) continue;
            if (image[dx][dy] == replaced_) {
                image[dx][dy] = newColor_;
                solve(image, dx, dy);
            }
        }
        return;
    }

    int rows_;
    int cols_;
    int replaced_;
    int newColor_;
};

int main() {
    return 0;
}