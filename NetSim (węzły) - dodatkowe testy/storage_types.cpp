#include "storage_types.hxx"

Package PackageQueue::pop() {
    Package p;

    if (type_ == PackageQueueType::FIFO) {
        p = std::move(*packages_.begin());
        packages_.erase(packages_.begin());
    } else {
        p = std::move(*packages_.rbegin());
        packages_.erase(--packages_.end());
    }

    return p;
}
