// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from roomie_msgs:msg/RoomiePose.idl
// generated code does not contain a copyright notice
#include "roomie_msgs/msg/detail/roomie_pose__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `pose`
#include "geometry_msgs/msg/detail/pose__functions.h"

bool
roomie_msgs__msg__RoomiePose__init(roomie_msgs__msg__RoomiePose * msg)
{
  if (!msg) {
    return false;
  }
  // robot_id
  // floor_id
  // pose
  if (!geometry_msgs__msg__Pose__init(&msg->pose)) {
    roomie_msgs__msg__RoomiePose__fini(msg);
    return false;
  }
  return true;
}

void
roomie_msgs__msg__RoomiePose__fini(roomie_msgs__msg__RoomiePose * msg)
{
  if (!msg) {
    return;
  }
  // robot_id
  // floor_id
  // pose
  geometry_msgs__msg__Pose__fini(&msg->pose);
}

bool
roomie_msgs__msg__RoomiePose__are_equal(const roomie_msgs__msg__RoomiePose * lhs, const roomie_msgs__msg__RoomiePose * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // robot_id
  if (lhs->robot_id != rhs->robot_id) {
    return false;
  }
  // floor_id
  if (lhs->floor_id != rhs->floor_id) {
    return false;
  }
  // pose
  if (!geometry_msgs__msg__Pose__are_equal(
      &(lhs->pose), &(rhs->pose)))
  {
    return false;
  }
  return true;
}

bool
roomie_msgs__msg__RoomiePose__copy(
  const roomie_msgs__msg__RoomiePose * input,
  roomie_msgs__msg__RoomiePose * output)
{
  if (!input || !output) {
    return false;
  }
  // robot_id
  output->robot_id = input->robot_id;
  // floor_id
  output->floor_id = input->floor_id;
  // pose
  if (!geometry_msgs__msg__Pose__copy(
      &(input->pose), &(output->pose)))
  {
    return false;
  }
  return true;
}

roomie_msgs__msg__RoomiePose *
roomie_msgs__msg__RoomiePose__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  roomie_msgs__msg__RoomiePose * msg = (roomie_msgs__msg__RoomiePose *)allocator.allocate(sizeof(roomie_msgs__msg__RoomiePose), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(roomie_msgs__msg__RoomiePose));
  bool success = roomie_msgs__msg__RoomiePose__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
roomie_msgs__msg__RoomiePose__destroy(roomie_msgs__msg__RoomiePose * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    roomie_msgs__msg__RoomiePose__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
roomie_msgs__msg__RoomiePose__Sequence__init(roomie_msgs__msg__RoomiePose__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  roomie_msgs__msg__RoomiePose * data = NULL;

  if (size) {
    data = (roomie_msgs__msg__RoomiePose *)allocator.zero_allocate(size, sizeof(roomie_msgs__msg__RoomiePose), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = roomie_msgs__msg__RoomiePose__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        roomie_msgs__msg__RoomiePose__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
roomie_msgs__msg__RoomiePose__Sequence__fini(roomie_msgs__msg__RoomiePose__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      roomie_msgs__msg__RoomiePose__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

roomie_msgs__msg__RoomiePose__Sequence *
roomie_msgs__msg__RoomiePose__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  roomie_msgs__msg__RoomiePose__Sequence * array = (roomie_msgs__msg__RoomiePose__Sequence *)allocator.allocate(sizeof(roomie_msgs__msg__RoomiePose__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = roomie_msgs__msg__RoomiePose__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
roomie_msgs__msg__RoomiePose__Sequence__destroy(roomie_msgs__msg__RoomiePose__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    roomie_msgs__msg__RoomiePose__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
roomie_msgs__msg__RoomiePose__Sequence__are_equal(const roomie_msgs__msg__RoomiePose__Sequence * lhs, const roomie_msgs__msg__RoomiePose__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!roomie_msgs__msg__RoomiePose__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
roomie_msgs__msg__RoomiePose__Sequence__copy(
  const roomie_msgs__msg__RoomiePose__Sequence * input,
  roomie_msgs__msg__RoomiePose__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(roomie_msgs__msg__RoomiePose);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    roomie_msgs__msg__RoomiePose * data =
      (roomie_msgs__msg__RoomiePose *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!roomie_msgs__msg__RoomiePose__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          roomie_msgs__msg__RoomiePose__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!roomie_msgs__msg__RoomiePose__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
