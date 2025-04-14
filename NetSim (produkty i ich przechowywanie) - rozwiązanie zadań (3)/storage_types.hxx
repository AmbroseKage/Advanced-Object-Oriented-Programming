#include "package.hxx"
#include <list>

enum class PackageQueueType {
    FIFO,
    LIFO
};

class IPackageStockpile {
public:
    using const_iterator = std::list<Package>::const_iterator;

    virtual void push(Package&& package) = 0;

    virtual std::size_t size() const = 0;
    
    virtual const_iterator begin() const = 0;
    virtual const_iterator end() const = 0;
    
    virtual bool empty() const = 0;
    
    virtual ~IPackageStockpile() = default;
    
};

class IPackageQueue : public IPackageStockpile {
public:
    virtual Package pop() = 0;
    virtual PackageQueueType get_queue_type() const = 0;
    virtual ~IPackageQueue() = default;
};

class PackageQueue : public IPackageQueue {
public:
    explicit PackageQueue(PackageQueueType type) : type_(type) {};

    void push(Package&& p) override {
        packages_.emplace_back(std::move(p));
    }
    
    std::size_t size() const override {
        return packages_.size();
    }
    
    const_iterator begin() const override {
        return packages_.begin();
    }
    const_iterator end() const override {
        return packages_.end();
    }
        
    bool empty() const override {
        return packages_.empty();
    }


    Package pop() override;
    
    PackageQueueType get_queue_type() const override {
        return type_;
    }

private:
    PackageQueueType type_;
    std::list<Package> packages_;
};