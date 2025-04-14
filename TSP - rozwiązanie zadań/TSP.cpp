#include "TSP.hxx"

#include <algorithm>
#include <stack>
#include <optional>

std::ostream &operator<<(std::ostream &os, const CostMatrix &cm) {
    for (std::size_t r = 0; r < cm.size(); ++r) {
        for (std::size_t c = 0; c < cm.size(); ++c) {
            const auto &elem = cm[r][c];
            os << (is_inf(elem) ? "INF" : std::to_string(elem)) << " ";
        }
        os << "\n";
    }
    os << std::endl;

    return os;
}


path_t StageState::get_path() {
    NewVertex vertex = choose_new_vertex();
    append_to_path(vertex.coordinates);
    update_cost_matrix(vertex.coordinates);
    for (int i = 0; i < matrix_.size(); i++) {
        for (int j = 0; j < matrix_.size(); j++) {
            if (matrix_[i][j] != INF) {
                append_to_path(vertex_t(i, j));
            }
        }
    }
    path_t sorted_path = {unsorted_path_[0].col};
    unsorted_path_[0].row = INF;
    while(sorted_path.size() != unsorted_path_.size()) {
        for (int i = 0; i < unsorted_path_.size(); i++) {
            if (unsorted_path_[i].row == sorted_path.back()) {
                sorted_path.push_back(unsorted_path_[i].col);
                unsorted_path_[i].row == INF;
            }
        }
    }

    return sorted_path;
}


std::vector<cost_t> CostMatrix::get_min_values_in_rows() const {
    std::vector<cost_t> min_value_vector = {};
    for (auto &row: matrix_) {
        cost_t min_value = INF;
        for (auto elem: row) {
            if (elem < min_value) {
                min_value = elem;
            }
        }
        if (min_value == INF) {
            min_value = 0;
        }
        min_value_vector.push_back(min_value);
    }
    return min_value_vector;
}

cost_t CostMatrix::reduce_rows() {
    cost_t sum = 0;
    std::vector<cost_t> min_vector = get_min_values_in_rows();
    for (int i = 0; i < matrix_.size(); i++) {
        for (int j = 0; j < matrix_[0].size(); j++) {
            if (matrix_[i][j] != INF) {
                matrix_[i][j] -= min_vector[i];
            }
        }
        sum += min_vector[i];
    }
    return sum;
}

std::vector<cost_t> CostMatrix::get_min_values_in_cols() const {
    std::vector<cost_t> min_value_vector = {};
    for (int j = 0; j < matrix_[0].size(); j++) {
        cost_t min_value = INF;
        for (int i = 0; i < matrix_.size(); i++) {
            if (matrix_[i][j] < min_value) {
                min_value = matrix_[i][j];
            }
        }
        if (min_value == INF) {
            min_value = 0;
        }
        min_value_vector.push_back(min_value);
    }
    return min_value_vector;
}

cost_t CostMatrix::reduce_cols() {
    cost_t sum = 0;
    std::vector<cost_t> min_vector = get_min_values_in_cols();
    for (int j = 0; j < matrix_[0].size(); j++) {
        for (int i = 0; i < matrix_.size(); i++) {
            if (matrix_[i][j] != INF) {
                matrix_[i][j] -= min_vector[j];
            }
        }
        sum += min_vector[j];
    }
    return sum;
}

cost_t CostMatrix::get_vertex_cost(std::size_t row, std::size_t col) const {
    cost_t min_value_r = INF;
    cost_t min_value_c = INF;
    for (int j = 0; j < matrix_[0].size(); j++) {
        if (j != col) {
            if (matrix_[row][j] < min_value_r) {
                min_value_r = matrix_[row][j];
            }
        }
    }
    for (int i = 0; i < matrix_.size(); i++) {
        if (i != row) {
            if (matrix_[i][col] < min_value_c) {
                min_value_c = matrix_[i][col];
            }
        }
    }
    return min_value_c + min_value_r;
}

NewVertex StageState::choose_new_vertex() {
    cost_t max_value = 0;
    vertex_t vertex;
    for (int i = 0; i < matrix_.size(); i++) {
        for (int j = 0; j < matrix_[0].size(); j++) {
            if (matrix_[i][j] == 0) {
                cost_t cost = matrix_.get_vertex_cost(i, j);
                if (cost > max_value) {
                    max_value = cost;
                    vertex.row = i;
                    vertex.col = j;
                }
            }
        }
    }
    return NewVertex(vertex, max_value);
}

void StageState::update_cost_matrix(vertex_t new_vertex) {
    for (int i = 0; i < matrix_.size(); i++) {
        for (int j = 0; j < matrix_[0].size(); j++) {
            if (i == new_vertex.row or j == new_vertex.col) {
                matrix_[i][j] = INF;
            }
        }
    }
    matrix_[new_vertex.col][new_vertex.row] = INF;

    if (unsorted_path_.size() != matrix_.size()) {
        std::vector<std::pair<int, bool>> vertexes_from = {};
        std::vector<std::pair<int, bool>> vertexes_to = {};
        for (auto &edge: unsorted_path_) {
            vertexes_from.push_back(std::make_pair(edge.row, false));
            vertexes_to.push_back(std::make_pair(edge.col, false));
        }
        for (int i = 0; i < vertexes_from.size(); i++) {
            for (int j = 0; j < vertexes_from.size(); j++) {
                if (vertexes_from[i] == vertexes_from[j] and i != j) {
                    vertexes_from[i].second = true;
                    vertexes_from[j].second = true;
                }
            }
        }
        int forbidden_from = INF;
        for (auto &vertex: vertexes_from) {
            if (!vertex.second) {
                forbidden_from = vertex.first;
            }
        }
        for (int i = 0; i < vertexes_to.size(); i++) {
            for (int j = 0; j < vertexes_to.size(); j++) {
                if (vertexes_to[i] == vertexes_to[j] and i != j) {
                    vertexes_to[i].second = true;
                    vertexes_to[j].second = true;
                }
            }
        }
        int forbidden_to = INF;
        for (auto &vertex: vertexes_to) {
            if (!vertex.second) {
                forbidden_to = vertex.first;
            }
        }
        matrix_[forbidden_from][forbidden_to] = INF;
    }
    return;
}

cost_t StageState::reduce_cost_matrix() {
    cost_t sum_r = matrix_.reduce_rows();
    cost_t sum_c = matrix_.reduce_cols();
    return sum_c + sum_r;
}

cost_t get_optimal_cost(const path_t &optimal_path, const cost_matrix_t &m) {
    cost_t cost = 0;

    for (std::size_t idx = 1; idx < optimal_path.size(); ++idx) {
        cost += m[optimal_path[idx - 1]][optimal_path[idx]];
    }

    cost += m[optimal_path[optimal_path.size() - 1]][optimal_path[0]];

    return cost;
}


StageState create_right_branch_matrix(cost_matrix_t m, vertex_t v, cost_t lb) {
    CostMatrix cm(m);
    cm[v.row][v.col] = INF;
    return StageState(cm, {}, lb);
}

tsp_solutions_t filter_solutions(tsp_solutions_t solutions) {
    cost_t optimal_cost = INF;
    for (const auto &s: solutions) {
        optimal_cost = (s.lower_bound < optimal_cost) ? s.lower_bound : optimal_cost;
    }

    tsp_solutions_t optimal_solutions;
    std::copy_if(solutions.begin(), solutions.end(),
                 std::back_inserter(optimal_solutions),
                 [&optimal_cost](const tsp_solution_t &s) { return s.lower_bound == optimal_cost; }
    );

    return optimal_solutions;
}

tsp_solutions_t solve_tsp(const cost_matrix_t &cm) {

    StageState left_branch(cm);

    std::stack<StageState> tree_lifo;

    std::size_t n_levels = cm.size() - 2;

    tree_lifo.push(left_branch); 

    cost_t best_lb = INF;
    tsp_solutions_t solutions;

    while (!tree_lifo.empty()) {

        left_branch = tree_lifo.top();
        tree_lifo.pop();

        while (left_branch.get_level() != n_levels && left_branch.get_lower_bound() <= best_lb) {

            if (left_branch.get_level() == 0) {
                left_branch.reset_lower_bound();
            }

            cost_t new_cost = 0;
            new_cost = left_branch.reduce_cost_matrix();


            left_branch.update_lower_bound(new_cost);
            if (left_branch.get_lower_bound() > best_lb) {
                break;
            }

            NewVertex new_vertex = NewVertex(); 
            new_vertex = left_branch.choose_new_vertex();

            left_branch.append_to_path(new_vertex.coordinates);

            left_branch.update_cost_matrix(new_vertex.coordinates);

            cost_t new_lower_bound = left_branch.get_lower_bound() + new_vertex.cost;
            tree_lifo.push(create_right_branch_matrix(cm, new_vertex.coordinates,
                                                      new_lower_bound));
        }

        if (left_branch.get_lower_bound() <= best_lb) {
            
            best_lb = left_branch.get_lower_bound();
            path_t new_path = left_branch.get_path();
            solutions.push_back({get_optimal_cost(new_path, cm), new_path});
        }
    }

    return filter_solutions(solutions);
}
