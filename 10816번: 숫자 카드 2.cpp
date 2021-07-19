#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int N;
    std::cin >> N;

    vector<int> v;
    int tmp;

    for (int i = 0; i < N; i++)
    {
    std:
        cin >> tmp;
        v.push_back(tmp);
    }

    sort(v.begin(), v.end());

    vector<int> ans;

    int M;
    std::cin >> M;

    for (int i = 0; i < M; i++)
    {
        std::cin >> tmp;
        auto upper = upper_bound(v.begin(), v.end(), tmp);
        auto lower = lower_bound(v.begin(), v.end(), tmp);
        ans.push_back(upper - lower);
    }

    for (int i = 0; i < ans.size(); i++)
        std::cout << ans[i] << " ";
}
