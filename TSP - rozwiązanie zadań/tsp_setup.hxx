//
// Created by pkleczek on 9/30/20.
//

#ifndef IMPLEMENTATION_INFINITY_HPP
#define IMPLEMENTATION_INFINITY_HPP

#include <limits>
#include <vector>

using cost_t = int;

const cost_t INF = std::numeric_limits<cost_t>::max();

bool is_inf(cost_t val);

using path_t = std::vector<std::size_t>;


class IStageState {
public:
    virtual path_t get_path() = 0;
    virtual std::size_t get_level() const = 0;
    virtual cost_t get_lower_bound() const = 0;
};

#endif
