// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from roomie_msgs:action/PerformTask.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "roomie_msgs/action/perform_task.hpp"


#ifndef ROOMIE_MSGS__ACTION__DETAIL__PERFORM_TASK__STRUCT_HPP_
#define ROOMIE_MSGS__ACTION__DETAIL__PERFORM_TASK__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__roomie_msgs__action__PerformTask_Goal __attribute__((deprecated))
#else
# define DEPRECATED__roomie_msgs__action__PerformTask_Goal __declspec(deprecated)
#endif

namespace roomie_msgs
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct PerformTask_Goal_
{
  using Type = PerformTask_Goal_<ContainerAllocator>;

  explicit PerformTask_Goal_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->robot_id = 0l;
      this->task_id = 0l;
      this->task_type_id = 0l;
      this->task_status_id = 0l;
      this->target_location_id = 0l;
      this->pickup_location_id = 0l;
      this->order_info = "";
    }
  }

  explicit PerformTask_Goal_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : order_info(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->robot_id = 0l;
      this->task_id = 0l;
      this->task_type_id = 0l;
      this->task_status_id = 0l;
      this->target_location_id = 0l;
      this->pickup_location_id = 0l;
      this->order_info = "";
    }
  }

  // field types and members
  using _robot_id_type =
    int32_t;
  _robot_id_type robot_id;
  using _task_id_type =
    int32_t;
  _task_id_type task_id;
  using _task_type_id_type =
    int32_t;
  _task_type_id_type task_type_id;
  using _task_status_id_type =
    int32_t;
  _task_status_id_type task_status_id;
  using _target_location_id_type =
    int32_t;
  _target_location_id_type target_location_id;
  using _pickup_location_id_type =
    int32_t;
  _pickup_location_id_type pickup_location_id;
  using _order_info_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _order_info_type order_info;

  // setters for named parameter idiom
  Type & set__robot_id(
    const int32_t & _arg)
  {
    this->robot_id = _arg;
    return *this;
  }
  Type & set__task_id(
    const int32_t & _arg)
  {
    this->task_id = _arg;
    return *this;
  }
  Type & set__task_type_id(
    const int32_t & _arg)
  {
    this->task_type_id = _arg;
    return *this;
  }
  Type & set__task_status_id(
    const int32_t & _arg)
  {
    this->task_status_id = _arg;
    return *this;
  }
  Type & set__target_location_id(
    const int32_t & _arg)
  {
    this->target_location_id = _arg;
    return *this;
  }
  Type & set__pickup_location_id(
    const int32_t & _arg)
  {
    this->pickup_location_id = _arg;
    return *this;
  }
  Type & set__order_info(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->order_info = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    roomie_msgs::action::PerformTask_Goal_<ContainerAllocator> *;
  using ConstRawPtr =
    const roomie_msgs::action::PerformTask_Goal_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<roomie_msgs::action::PerformTask_Goal_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<roomie_msgs::action::PerformTask_Goal_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      roomie_msgs::action::PerformTask_Goal_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<roomie_msgs::action::PerformTask_Goal_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      roomie_msgs::action::PerformTask_Goal_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<roomie_msgs::action::PerformTask_Goal_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<roomie_msgs::action::PerformTask_Goal_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<roomie_msgs::action::PerformTask_Goal_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__roomie_msgs__action__PerformTask_Goal
    std::shared_ptr<roomie_msgs::action::PerformTask_Goal_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__roomie_msgs__action__PerformTask_Goal
    std::shared_ptr<roomie_msgs::action::PerformTask_Goal_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const PerformTask_Goal_ & other) const
  {
    if (this->robot_id != other.robot_id) {
      return false;
    }
    if (this->task_id != other.task_id) {
      return false;
    }
    if (this->task_type_id != other.task_type_id) {
      return false;
    }
    if (this->task_status_id != other.task_status_id) {
      return false;
    }
    if (this->target_location_id != other.target_location_id) {
      return false;
    }
    if (this->pickup_location_id != other.pickup_location_id) {
      return false;
    }
    if (this->order_info != other.order_info) {
      return false;
    }
    return true;
  }
  bool operator!=(const PerformTask_Goal_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct PerformTask_Goal_

// alias to use template instance with default allocator
using PerformTask_Goal =
  roomie_msgs::action::PerformTask_Goal_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace roomie_msgs


#ifndef _WIN32
# define DEPRECATED__roomie_msgs__action__PerformTask_Result __attribute__((deprecated))
#else
# define DEPRECATED__roomie_msgs__action__PerformTask_Result __declspec(deprecated)
#endif

namespace roomie_msgs
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct PerformTask_Result_
{
  using Type = PerformTask_Result_<ContainerAllocator>;

  explicit PerformTask_Result_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->robot_id = 0l;
      this->task_id = 0l;
      this->success = false;
      this->message = "";
    }
  }

  explicit PerformTask_Result_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : message(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->robot_id = 0l;
      this->task_id = 0l;
      this->success = false;
      this->message = "";
    }
  }

  // field types and members
  using _robot_id_type =
    int32_t;
  _robot_id_type robot_id;
  using _task_id_type =
    int32_t;
  _task_id_type task_id;
  using _success_type =
    bool;
  _success_type success;
  using _message_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _message_type message;

  // setters for named parameter idiom
  Type & set__robot_id(
    const int32_t & _arg)
  {
    this->robot_id = _arg;
    return *this;
  }
  Type & set__task_id(
    const int32_t & _arg)
  {
    this->task_id = _arg;
    return *this;
  }
  Type & set__success(
    const bool & _arg)
  {
    this->success = _arg;
    return *this;
  }
  Type & set__message(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->message = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    roomie_msgs::action::PerformTask_Result_<ContainerAllocator> *;
  using ConstRawPtr =
    const roomie_msgs::action::PerformTask_Result_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<roomie_msgs::action::PerformTask_Result_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<roomie_msgs::action::PerformTask_Result_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      roomie_msgs::action::PerformTask_Result_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<roomie_msgs::action::PerformTask_Result_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      roomie_msgs::action::PerformTask_Result_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<roomie_msgs::action::PerformTask_Result_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<roomie_msgs::action::PerformTask_Result_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<roomie_msgs::action::PerformTask_Result_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__roomie_msgs__action__PerformTask_Result
    std::shared_ptr<roomie_msgs::action::PerformTask_Result_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__roomie_msgs__action__PerformTask_Result
    std::shared_ptr<roomie_msgs::action::PerformTask_Result_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const PerformTask_Result_ & other) const
  {
    if (this->robot_id != other.robot_id) {
      return false;
    }
    if (this->task_id != other.task_id) {
      return false;
    }
    if (this->success != other.success) {
      return false;
    }
    if (this->message != other.message) {
      return false;
    }
    return true;
  }
  bool operator!=(const PerformTask_Result_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct PerformTask_Result_

// alias to use template instance with default allocator
using PerformTask_Result =
  roomie_msgs::action::PerformTask_Result_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace roomie_msgs


#ifndef _WIN32
# define DEPRECATED__roomie_msgs__action__PerformTask_Feedback __attribute__((deprecated))
#else
# define DEPRECATED__roomie_msgs__action__PerformTask_Feedback __declspec(deprecated)
#endif

namespace roomie_msgs
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct PerformTask_Feedback_
{
  using Type = PerformTask_Feedback_<ContainerAllocator>;

  explicit PerformTask_Feedback_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->robot_id = 0l;
      this->task_id = 0l;
      this->task_status_id = 0l;
    }
  }

  explicit PerformTask_Feedback_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->robot_id = 0l;
      this->task_id = 0l;
      this->task_status_id = 0l;
    }
  }

  // field types and members
  using _robot_id_type =
    int32_t;
  _robot_id_type robot_id;
  using _task_id_type =
    int32_t;
  _task_id_type task_id;
  using _task_status_id_type =
    int32_t;
  _task_status_id_type task_status_id;

  // setters for named parameter idiom
  Type & set__robot_id(
    const int32_t & _arg)
  {
    this->robot_id = _arg;
    return *this;
  }
  Type & set__task_id(
    const int32_t & _arg)
  {
    this->task_id = _arg;
    return *this;
  }
  Type & set__task_status_id(
    const int32_t & _arg)
  {
    this->task_status_id = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    roomie_msgs::action::PerformTask_Feedback_<ContainerAllocator> *;
  using ConstRawPtr =
    const roomie_msgs::action::PerformTask_Feedback_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<roomie_msgs::action::PerformTask_Feedback_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<roomie_msgs::action::PerformTask_Feedback_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      roomie_msgs::action::PerformTask_Feedback_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<roomie_msgs::action::PerformTask_Feedback_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      roomie_msgs::action::PerformTask_Feedback_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<roomie_msgs::action::PerformTask_Feedback_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<roomie_msgs::action::PerformTask_Feedback_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<roomie_msgs::action::PerformTask_Feedback_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__roomie_msgs__action__PerformTask_Feedback
    std::shared_ptr<roomie_msgs::action::PerformTask_Feedback_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__roomie_msgs__action__PerformTask_Feedback
    std::shared_ptr<roomie_msgs::action::PerformTask_Feedback_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const PerformTask_Feedback_ & other) const
  {
    if (this->robot_id != other.robot_id) {
      return false;
    }
    if (this->task_id != other.task_id) {
      return false;
    }
    if (this->task_status_id != other.task_status_id) {
      return false;
    }
    return true;
  }
  bool operator!=(const PerformTask_Feedback_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct PerformTask_Feedback_

// alias to use template instance with default allocator
using PerformTask_Feedback =
  roomie_msgs::action::PerformTask_Feedback_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace roomie_msgs


// Include directives for member types
// Member 'goal_id'
#include "unique_identifier_msgs/msg/detail/uuid__struct.hpp"
// Member 'goal'
#include "roomie_msgs/action/detail/perform_task__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__roomie_msgs__action__PerformTask_SendGoal_Request __attribute__((deprecated))
#else
# define DEPRECATED__roomie_msgs__action__PerformTask_SendGoal_Request __declspec(deprecated)
#endif

namespace roomie_msgs
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct PerformTask_SendGoal_Request_
{
  using Type = PerformTask_SendGoal_Request_<ContainerAllocator>;

  explicit PerformTask_SendGoal_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : goal_id(_init),
    goal(_init)
  {
    (void)_init;
  }

  explicit PerformTask_SendGoal_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : goal_id(_alloc, _init),
    goal(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _goal_id_type =
    unique_identifier_msgs::msg::UUID_<ContainerAllocator>;
  _goal_id_type goal_id;
  using _goal_type =
    roomie_msgs::action::PerformTask_Goal_<ContainerAllocator>;
  _goal_type goal;

  // setters for named parameter idiom
  Type & set__goal_id(
    const unique_identifier_msgs::msg::UUID_<ContainerAllocator> & _arg)
  {
    this->goal_id = _arg;
    return *this;
  }
  Type & set__goal(
    const roomie_msgs::action::PerformTask_Goal_<ContainerAllocator> & _arg)
  {
    this->goal = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    roomie_msgs::action::PerformTask_SendGoal_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const roomie_msgs::action::PerformTask_SendGoal_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<roomie_msgs::action::PerformTask_SendGoal_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<roomie_msgs::action::PerformTask_SendGoal_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      roomie_msgs::action::PerformTask_SendGoal_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<roomie_msgs::action::PerformTask_SendGoal_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      roomie_msgs::action::PerformTask_SendGoal_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<roomie_msgs::action::PerformTask_SendGoal_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<roomie_msgs::action::PerformTask_SendGoal_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<roomie_msgs::action::PerformTask_SendGoal_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__roomie_msgs__action__PerformTask_SendGoal_Request
    std::shared_ptr<roomie_msgs::action::PerformTask_SendGoal_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__roomie_msgs__action__PerformTask_SendGoal_Request
    std::shared_ptr<roomie_msgs::action::PerformTask_SendGoal_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const PerformTask_SendGoal_Request_ & other) const
  {
    if (this->goal_id != other.goal_id) {
      return false;
    }
    if (this->goal != other.goal) {
      return false;
    }
    return true;
  }
  bool operator!=(const PerformTask_SendGoal_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct PerformTask_SendGoal_Request_

// alias to use template instance with default allocator
using PerformTask_SendGoal_Request =
  roomie_msgs::action::PerformTask_SendGoal_Request_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace roomie_msgs


// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__roomie_msgs__action__PerformTask_SendGoal_Response __attribute__((deprecated))
#else
# define DEPRECATED__roomie_msgs__action__PerformTask_SendGoal_Response __declspec(deprecated)
#endif

namespace roomie_msgs
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct PerformTask_SendGoal_Response_
{
  using Type = PerformTask_SendGoal_Response_<ContainerAllocator>;

  explicit PerformTask_SendGoal_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : stamp(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->accepted = false;
    }
  }

  explicit PerformTask_SendGoal_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : stamp(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->accepted = false;
    }
  }

  // field types and members
  using _accepted_type =
    bool;
  _accepted_type accepted;
  using _stamp_type =
    builtin_interfaces::msg::Time_<ContainerAllocator>;
  _stamp_type stamp;

  // setters for named parameter idiom
  Type & set__accepted(
    const bool & _arg)
  {
    this->accepted = _arg;
    return *this;
  }
  Type & set__stamp(
    const builtin_interfaces::msg::Time_<ContainerAllocator> & _arg)
  {
    this->stamp = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    roomie_msgs::action::PerformTask_SendGoal_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const roomie_msgs::action::PerformTask_SendGoal_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<roomie_msgs::action::PerformTask_SendGoal_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<roomie_msgs::action::PerformTask_SendGoal_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      roomie_msgs::action::PerformTask_SendGoal_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<roomie_msgs::action::PerformTask_SendGoal_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      roomie_msgs::action::PerformTask_SendGoal_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<roomie_msgs::action::PerformTask_SendGoal_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<roomie_msgs::action::PerformTask_SendGoal_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<roomie_msgs::action::PerformTask_SendGoal_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__roomie_msgs__action__PerformTask_SendGoal_Response
    std::shared_ptr<roomie_msgs::action::PerformTask_SendGoal_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__roomie_msgs__action__PerformTask_SendGoal_Response
    std::shared_ptr<roomie_msgs::action::PerformTask_SendGoal_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const PerformTask_SendGoal_Response_ & other) const
  {
    if (this->accepted != other.accepted) {
      return false;
    }
    if (this->stamp != other.stamp) {
      return false;
    }
    return true;
  }
  bool operator!=(const PerformTask_SendGoal_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct PerformTask_SendGoal_Response_

// alias to use template instance with default allocator
using PerformTask_SendGoal_Response =
  roomie_msgs::action::PerformTask_SendGoal_Response_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace roomie_msgs


// Include directives for member types
// Member 'info'
#include "service_msgs/msg/detail/service_event_info__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__roomie_msgs__action__PerformTask_SendGoal_Event __attribute__((deprecated))
#else
# define DEPRECATED__roomie_msgs__action__PerformTask_SendGoal_Event __declspec(deprecated)
#endif

namespace roomie_msgs
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct PerformTask_SendGoal_Event_
{
  using Type = PerformTask_SendGoal_Event_<ContainerAllocator>;

  explicit PerformTask_SendGoal_Event_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : info(_init)
  {
    (void)_init;
  }

  explicit PerformTask_SendGoal_Event_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : info(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _info_type =
    service_msgs::msg::ServiceEventInfo_<ContainerAllocator>;
  _info_type info;
  using _request_type =
    rosidl_runtime_cpp::BoundedVector<roomie_msgs::action::PerformTask_SendGoal_Request_<ContainerAllocator>, 1, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<roomie_msgs::action::PerformTask_SendGoal_Request_<ContainerAllocator>>>;
  _request_type request;
  using _response_type =
    rosidl_runtime_cpp::BoundedVector<roomie_msgs::action::PerformTask_SendGoal_Response_<ContainerAllocator>, 1, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<roomie_msgs::action::PerformTask_SendGoal_Response_<ContainerAllocator>>>;
  _response_type response;

  // setters for named parameter idiom
  Type & set__info(
    const service_msgs::msg::ServiceEventInfo_<ContainerAllocator> & _arg)
  {
    this->info = _arg;
    return *this;
  }
  Type & set__request(
    const rosidl_runtime_cpp::BoundedVector<roomie_msgs::action::PerformTask_SendGoal_Request_<ContainerAllocator>, 1, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<roomie_msgs::action::PerformTask_SendGoal_Request_<ContainerAllocator>>> & _arg)
  {
    this->request = _arg;
    return *this;
  }
  Type & set__response(
    const rosidl_runtime_cpp::BoundedVector<roomie_msgs::action::PerformTask_SendGoal_Response_<ContainerAllocator>, 1, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<roomie_msgs::action::PerformTask_SendGoal_Response_<ContainerAllocator>>> & _arg)
  {
    this->response = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    roomie_msgs::action::PerformTask_SendGoal_Event_<ContainerAllocator> *;
  using ConstRawPtr =
    const roomie_msgs::action::PerformTask_SendGoal_Event_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<roomie_msgs::action::PerformTask_SendGoal_Event_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<roomie_msgs::action::PerformTask_SendGoal_Event_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      roomie_msgs::action::PerformTask_SendGoal_Event_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<roomie_msgs::action::PerformTask_SendGoal_Event_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      roomie_msgs::action::PerformTask_SendGoal_Event_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<roomie_msgs::action::PerformTask_SendGoal_Event_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<roomie_msgs::action::PerformTask_SendGoal_Event_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<roomie_msgs::action::PerformTask_SendGoal_Event_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__roomie_msgs__action__PerformTask_SendGoal_Event
    std::shared_ptr<roomie_msgs::action::PerformTask_SendGoal_Event_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__roomie_msgs__action__PerformTask_SendGoal_Event
    std::shared_ptr<roomie_msgs::action::PerformTask_SendGoal_Event_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const PerformTask_SendGoal_Event_ & other) const
  {
    if (this->info != other.info) {
      return false;
    }
    if (this->request != other.request) {
      return false;
    }
    if (this->response != other.response) {
      return false;
    }
    return true;
  }
  bool operator!=(const PerformTask_SendGoal_Event_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct PerformTask_SendGoal_Event_

// alias to use template instance with default allocator
using PerformTask_SendGoal_Event =
  roomie_msgs::action::PerformTask_SendGoal_Event_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace roomie_msgs

namespace roomie_msgs
{

namespace action
{

struct PerformTask_SendGoal
{
  using Request = roomie_msgs::action::PerformTask_SendGoal_Request;
  using Response = roomie_msgs::action::PerformTask_SendGoal_Response;
  using Event = roomie_msgs::action::PerformTask_SendGoal_Event;
};

}  // namespace action

}  // namespace roomie_msgs


// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__roomie_msgs__action__PerformTask_GetResult_Request __attribute__((deprecated))
#else
# define DEPRECATED__roomie_msgs__action__PerformTask_GetResult_Request __declspec(deprecated)
#endif

namespace roomie_msgs
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct PerformTask_GetResult_Request_
{
  using Type = PerformTask_GetResult_Request_<ContainerAllocator>;

  explicit PerformTask_GetResult_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : goal_id(_init)
  {
    (void)_init;
  }

  explicit PerformTask_GetResult_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : goal_id(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _goal_id_type =
    unique_identifier_msgs::msg::UUID_<ContainerAllocator>;
  _goal_id_type goal_id;

  // setters for named parameter idiom
  Type & set__goal_id(
    const unique_identifier_msgs::msg::UUID_<ContainerAllocator> & _arg)
  {
    this->goal_id = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    roomie_msgs::action::PerformTask_GetResult_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const roomie_msgs::action::PerformTask_GetResult_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<roomie_msgs::action::PerformTask_GetResult_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<roomie_msgs::action::PerformTask_GetResult_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      roomie_msgs::action::PerformTask_GetResult_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<roomie_msgs::action::PerformTask_GetResult_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      roomie_msgs::action::PerformTask_GetResult_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<roomie_msgs::action::PerformTask_GetResult_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<roomie_msgs::action::PerformTask_GetResult_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<roomie_msgs::action::PerformTask_GetResult_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__roomie_msgs__action__PerformTask_GetResult_Request
    std::shared_ptr<roomie_msgs::action::PerformTask_GetResult_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__roomie_msgs__action__PerformTask_GetResult_Request
    std::shared_ptr<roomie_msgs::action::PerformTask_GetResult_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const PerformTask_GetResult_Request_ & other) const
  {
    if (this->goal_id != other.goal_id) {
      return false;
    }
    return true;
  }
  bool operator!=(const PerformTask_GetResult_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct PerformTask_GetResult_Request_

// alias to use template instance with default allocator
using PerformTask_GetResult_Request =
  roomie_msgs::action::PerformTask_GetResult_Request_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace roomie_msgs


// Include directives for member types
// Member 'result'
// already included above
// #include "roomie_msgs/action/detail/perform_task__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__roomie_msgs__action__PerformTask_GetResult_Response __attribute__((deprecated))
#else
# define DEPRECATED__roomie_msgs__action__PerformTask_GetResult_Response __declspec(deprecated)
#endif

namespace roomie_msgs
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct PerformTask_GetResult_Response_
{
  using Type = PerformTask_GetResult_Response_<ContainerAllocator>;

  explicit PerformTask_GetResult_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : result(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->status = 0;
    }
  }

  explicit PerformTask_GetResult_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : result(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->status = 0;
    }
  }

  // field types and members
  using _status_type =
    int8_t;
  _status_type status;
  using _result_type =
    roomie_msgs::action::PerformTask_Result_<ContainerAllocator>;
  _result_type result;

  // setters for named parameter idiom
  Type & set__status(
    const int8_t & _arg)
  {
    this->status = _arg;
    return *this;
  }
  Type & set__result(
    const roomie_msgs::action::PerformTask_Result_<ContainerAllocator> & _arg)
  {
    this->result = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    roomie_msgs::action::PerformTask_GetResult_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const roomie_msgs::action::PerformTask_GetResult_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<roomie_msgs::action::PerformTask_GetResult_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<roomie_msgs::action::PerformTask_GetResult_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      roomie_msgs::action::PerformTask_GetResult_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<roomie_msgs::action::PerformTask_GetResult_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      roomie_msgs::action::PerformTask_GetResult_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<roomie_msgs::action::PerformTask_GetResult_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<roomie_msgs::action::PerformTask_GetResult_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<roomie_msgs::action::PerformTask_GetResult_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__roomie_msgs__action__PerformTask_GetResult_Response
    std::shared_ptr<roomie_msgs::action::PerformTask_GetResult_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__roomie_msgs__action__PerformTask_GetResult_Response
    std::shared_ptr<roomie_msgs::action::PerformTask_GetResult_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const PerformTask_GetResult_Response_ & other) const
  {
    if (this->status != other.status) {
      return false;
    }
    if (this->result != other.result) {
      return false;
    }
    return true;
  }
  bool operator!=(const PerformTask_GetResult_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct PerformTask_GetResult_Response_

// alias to use template instance with default allocator
using PerformTask_GetResult_Response =
  roomie_msgs::action::PerformTask_GetResult_Response_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace roomie_msgs


// Include directives for member types
// Member 'info'
// already included above
// #include "service_msgs/msg/detail/service_event_info__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__roomie_msgs__action__PerformTask_GetResult_Event __attribute__((deprecated))
#else
# define DEPRECATED__roomie_msgs__action__PerformTask_GetResult_Event __declspec(deprecated)
#endif

namespace roomie_msgs
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct PerformTask_GetResult_Event_
{
  using Type = PerformTask_GetResult_Event_<ContainerAllocator>;

  explicit PerformTask_GetResult_Event_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : info(_init)
  {
    (void)_init;
  }

  explicit PerformTask_GetResult_Event_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : info(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _info_type =
    service_msgs::msg::ServiceEventInfo_<ContainerAllocator>;
  _info_type info;
  using _request_type =
    rosidl_runtime_cpp::BoundedVector<roomie_msgs::action::PerformTask_GetResult_Request_<ContainerAllocator>, 1, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<roomie_msgs::action::PerformTask_GetResult_Request_<ContainerAllocator>>>;
  _request_type request;
  using _response_type =
    rosidl_runtime_cpp::BoundedVector<roomie_msgs::action::PerformTask_GetResult_Response_<ContainerAllocator>, 1, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<roomie_msgs::action::PerformTask_GetResult_Response_<ContainerAllocator>>>;
  _response_type response;

  // setters for named parameter idiom
  Type & set__info(
    const service_msgs::msg::ServiceEventInfo_<ContainerAllocator> & _arg)
  {
    this->info = _arg;
    return *this;
  }
  Type & set__request(
    const rosidl_runtime_cpp::BoundedVector<roomie_msgs::action::PerformTask_GetResult_Request_<ContainerAllocator>, 1, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<roomie_msgs::action::PerformTask_GetResult_Request_<ContainerAllocator>>> & _arg)
  {
    this->request = _arg;
    return *this;
  }
  Type & set__response(
    const rosidl_runtime_cpp::BoundedVector<roomie_msgs::action::PerformTask_GetResult_Response_<ContainerAllocator>, 1, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<roomie_msgs::action::PerformTask_GetResult_Response_<ContainerAllocator>>> & _arg)
  {
    this->response = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    roomie_msgs::action::PerformTask_GetResult_Event_<ContainerAllocator> *;
  using ConstRawPtr =
    const roomie_msgs::action::PerformTask_GetResult_Event_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<roomie_msgs::action::PerformTask_GetResult_Event_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<roomie_msgs::action::PerformTask_GetResult_Event_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      roomie_msgs::action::PerformTask_GetResult_Event_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<roomie_msgs::action::PerformTask_GetResult_Event_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      roomie_msgs::action::PerformTask_GetResult_Event_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<roomie_msgs::action::PerformTask_GetResult_Event_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<roomie_msgs::action::PerformTask_GetResult_Event_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<roomie_msgs::action::PerformTask_GetResult_Event_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__roomie_msgs__action__PerformTask_GetResult_Event
    std::shared_ptr<roomie_msgs::action::PerformTask_GetResult_Event_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__roomie_msgs__action__PerformTask_GetResult_Event
    std::shared_ptr<roomie_msgs::action::PerformTask_GetResult_Event_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const PerformTask_GetResult_Event_ & other) const
  {
    if (this->info != other.info) {
      return false;
    }
    if (this->request != other.request) {
      return false;
    }
    if (this->response != other.response) {
      return false;
    }
    return true;
  }
  bool operator!=(const PerformTask_GetResult_Event_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct PerformTask_GetResult_Event_

// alias to use template instance with default allocator
using PerformTask_GetResult_Event =
  roomie_msgs::action::PerformTask_GetResult_Event_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace roomie_msgs

namespace roomie_msgs
{

namespace action
{

struct PerformTask_GetResult
{
  using Request = roomie_msgs::action::PerformTask_GetResult_Request;
  using Response = roomie_msgs::action::PerformTask_GetResult_Response;
  using Event = roomie_msgs::action::PerformTask_GetResult_Event;
};

}  // namespace action

}  // namespace roomie_msgs


// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.hpp"
// Member 'feedback'
// already included above
// #include "roomie_msgs/action/detail/perform_task__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__roomie_msgs__action__PerformTask_FeedbackMessage __attribute__((deprecated))
#else
# define DEPRECATED__roomie_msgs__action__PerformTask_FeedbackMessage __declspec(deprecated)
#endif

namespace roomie_msgs
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct PerformTask_FeedbackMessage_
{
  using Type = PerformTask_FeedbackMessage_<ContainerAllocator>;

  explicit PerformTask_FeedbackMessage_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : goal_id(_init),
    feedback(_init)
  {
    (void)_init;
  }

  explicit PerformTask_FeedbackMessage_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : goal_id(_alloc, _init),
    feedback(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _goal_id_type =
    unique_identifier_msgs::msg::UUID_<ContainerAllocator>;
  _goal_id_type goal_id;
  using _feedback_type =
    roomie_msgs::action::PerformTask_Feedback_<ContainerAllocator>;
  _feedback_type feedback;

  // setters for named parameter idiom
  Type & set__goal_id(
    const unique_identifier_msgs::msg::UUID_<ContainerAllocator> & _arg)
  {
    this->goal_id = _arg;
    return *this;
  }
  Type & set__feedback(
    const roomie_msgs::action::PerformTask_Feedback_<ContainerAllocator> & _arg)
  {
    this->feedback = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    roomie_msgs::action::PerformTask_FeedbackMessage_<ContainerAllocator> *;
  using ConstRawPtr =
    const roomie_msgs::action::PerformTask_FeedbackMessage_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<roomie_msgs::action::PerformTask_FeedbackMessage_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<roomie_msgs::action::PerformTask_FeedbackMessage_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      roomie_msgs::action::PerformTask_FeedbackMessage_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<roomie_msgs::action::PerformTask_FeedbackMessage_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      roomie_msgs::action::PerformTask_FeedbackMessage_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<roomie_msgs::action::PerformTask_FeedbackMessage_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<roomie_msgs::action::PerformTask_FeedbackMessage_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<roomie_msgs::action::PerformTask_FeedbackMessage_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__roomie_msgs__action__PerformTask_FeedbackMessage
    std::shared_ptr<roomie_msgs::action::PerformTask_FeedbackMessage_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__roomie_msgs__action__PerformTask_FeedbackMessage
    std::shared_ptr<roomie_msgs::action::PerformTask_FeedbackMessage_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const PerformTask_FeedbackMessage_ & other) const
  {
    if (this->goal_id != other.goal_id) {
      return false;
    }
    if (this->feedback != other.feedback) {
      return false;
    }
    return true;
  }
  bool operator!=(const PerformTask_FeedbackMessage_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct PerformTask_FeedbackMessage_

// alias to use template instance with default allocator
using PerformTask_FeedbackMessage =
  roomie_msgs::action::PerformTask_FeedbackMessage_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace roomie_msgs

#include "action_msgs/srv/cancel_goal.hpp"
#include "action_msgs/msg/goal_info.hpp"
#include "action_msgs/msg/goal_status_array.hpp"

namespace roomie_msgs
{

namespace action
{

struct PerformTask
{
  /// The goal message defined in the action definition.
  using Goal = roomie_msgs::action::PerformTask_Goal;
  /// The result message defined in the action definition.
  using Result = roomie_msgs::action::PerformTask_Result;
  /// The feedback message defined in the action definition.
  using Feedback = roomie_msgs::action::PerformTask_Feedback;

  struct Impl
  {
    /// The send_goal service using a wrapped version of the goal message as a request.
    using SendGoalService = roomie_msgs::action::PerformTask_SendGoal;
    /// The get_result service using a wrapped version of the result message as a response.
    using GetResultService = roomie_msgs::action::PerformTask_GetResult;
    /// The feedback message with generic fields which wraps the feedback message.
    using FeedbackMessage = roomie_msgs::action::PerformTask_FeedbackMessage;

    /// The generic service to cancel a goal.
    using CancelGoalService = action_msgs::srv::CancelGoal;
    /// The generic message for the status of a goal.
    using GoalStatusMessage = action_msgs::msg::GoalStatusArray;
  };
};

typedef struct PerformTask PerformTask;

}  // namespace action

}  // namespace roomie_msgs

#endif  // ROOMIE_MSGS__ACTION__DETAIL__PERFORM_TASK__STRUCT_HPP_
