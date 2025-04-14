#include "package.hxx"

std::set<ElementID> Package::assigned_IDs = {};
std::set<ElementID> Package::freed_IDs = {};

Package::Package() {
    if (!freed_IDs.empty()){
        id_ = *freed_IDs.begin();
        freed_IDs.erase(*freed_IDs.begin());
    }else{
        if(assigned_IDs.empty()){
            id_ = 1;
        }else{
            id_ = *assigned_IDs.rbegin() + 1;
        }
    }
    assigned_IDs.insert(id_);
}

Package::~Package() {
    freed_IDs.insert(id_);
    assigned_IDs.erase(id_);
}

