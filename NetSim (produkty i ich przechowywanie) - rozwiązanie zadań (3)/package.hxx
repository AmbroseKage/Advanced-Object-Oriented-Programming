#pragma once

#include "types.hxx"
#include <set>

class Package {
public:
    Package();
    explicit Package(ElementID id)  : id_(id) {assigned_IDs.insert(id); };
    ElementID get_id() const {return id_; };

    ~Package();

private:
    ElementID id_;
    static std::set<ElementID> assigned_IDs;
    static std::set<ElementID> freed_IDs;
};