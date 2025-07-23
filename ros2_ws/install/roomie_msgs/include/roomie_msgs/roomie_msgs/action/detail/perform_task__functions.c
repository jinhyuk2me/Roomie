// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from roomie_msgs:action/PerformTask.idl
// generated code does not contain a copyright notice
#include "roomie_msgs/action/detail/perform_task__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `order_info`
#include "rosidl_runtime_c/string_functions.h"

bool
roomie_msgs__action__PerformTask_Goal__init(roomie_msgs__action__PerformTask_Goal * msg)
{
  if (!msg) {
    return false;
  }
  // robot_id
  // task_id
  // task_type_id
  // task_status_id
  // target_location_id
  // pickup_location_id
  // order_info
  if (!rosidl_runtime_c__String__init(&msg->order_info)) {
    roomie_msgs__action__PerformTask_Goal__fini(msg);
    return false;
  }
  return true;
}

void
roomie_msgs__action__PerformTask_Goal__fini(roomie_msgs__action__PerformTask_Goal * msg)
{
  if (!msg) {
    return;
  }
  // robot_id
  // task_id
  // task_type_id
  // task_status_id
  // target_location_id
  // pickup_location_id
  // order_info
  rosidl_runtime_c__String__fini(&msg->order_info);
}

bool
roomie_msgs__action__PerformTask_Goal__are_equal(const roomie_msgs__action__PerformTask_Goal * lhs, const roomie_msgs__action__PerformTask_Goal * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // robot_id
  if (lhs->robot_id != rhs->robot_id) {
    return false;
  }
  // task_id
  if (lhs->task_id != rhs->task_id) {
    return false;
  }
  // task_type_id
  if (lhs->task_type_id != rhs->task_type_id) {
    return false;
  }
  // task_status_id
  if (lhs->task_status_id != rhs->task_status_id) {
    return false;
  }
  // target_location_id
  if (lhs->target_location_id != rhs->target_location_id) {
    return false;
  }
  // pickup_location_id
  if (lhs->pickup_location_id != rhs->pickup_location_id) {
    return false;
  }
  // order_info
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->order_info), &(rhs->order_info)))
  {
    return false;
  }
  return true;
}

bool
roomie_msgs__action__PerformTask_Goal__copy(
  const roomie_msgs__action__PerformTask_Goal * input,
  roomie_msgs__action__PerformTask_Goal * output)
{
  if (!input || !output) {
    return false;
  }
  // robot_id
  output->robot_id = input->robot_id;
  // task_id
  output->task_id = input->task_id;
  // task_type_id
  output->task_type_id = input->task_type_id;
  // task_status_id
  output->task_status_id = input->task_status_id;
  // target_location_id
  output->target_location_id = input->target_location_id;
  // pickup_location_id
  output->pickup_location_id = input->pickup_location_id;
  // order_info
  if (!rosidl_runtime_c__String__copy(
      &(input->order_info), &(output->order_info)))
  {
    return false;
  }
  return true;
}

roomie_msgs__action__PerformTask_Goal *
roomie_msgs__action__PerformTask_Goal__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  roomie_msgs__action__PerformTask_Goal * msg = (roomie_msgs__action__PerformTask_Goal *)allocator.allocate(sizeof(roomie_msgs__action__PerformTask_Goal), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(roomie_msgs__action__PerformTask_Goal));
  bool success = roomie_msgs__action__PerformTask_Goal__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
roomie_msgs__action__PerformTask_Goal__destroy(roomie_msgs__action__PerformTask_Goal * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    roomie_msgs__action__PerformTask_Goal__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
roomie_msgs__action__PerformTask_Goal__Sequence__init(roomie_msgs__action__PerformTask_Goal__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  roomie_msgs__action__PerformTask_Goal * data = NULL;

  if (size) {
    data = (roomie_msgs__action__PerformTask_Goal *)allocator.zero_allocate(size, sizeof(roomie_msgs__action__PerformTask_Goal), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = roomie_msgs__action__PerformTask_Goal__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        roomie_msgs__action__PerformTask_Goal__fini(&data[i - 1]);
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
roomie_msgs__action__PerformTask_Goal__Sequence__fini(roomie_msgs__action__PerformTask_Goal__Sequence * array)
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
      roomie_msgs__action__PerformTask_Goal__fini(&array->data[i]);
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

roomie_msgs__action__PerformTask_Goal__Sequence *
roomie_msgs__action__PerformTask_Goal__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  roomie_msgs__action__PerformTask_Goal__Sequence * array = (roomie_msgs__action__PerformTask_Goal__Sequence *)allocator.allocate(sizeof(roomie_msgs__action__PerformTask_Goal__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = roomie_msgs__action__PerformTask_Goal__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
roomie_msgs__action__PerformTask_Goal__Sequence__destroy(roomie_msgs__action__PerformTask_Goal__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    roomie_msgs__action__PerformTask_Goal__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
roomie_msgs__action__PerformTask_Goal__Sequence__are_equal(const roomie_msgs__action__PerformTask_Goal__Sequence * lhs, const roomie_msgs__action__PerformTask_Goal__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!roomie_msgs__action__PerformTask_Goal__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
roomie_msgs__action__PerformTask_Goal__Sequence__copy(
  const roomie_msgs__action__PerformTask_Goal__Sequence * input,
  roomie_msgs__action__PerformTask_Goal__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(roomie_msgs__action__PerformTask_Goal);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    roomie_msgs__action__PerformTask_Goal * data =
      (roomie_msgs__action__PerformTask_Goal *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!roomie_msgs__action__PerformTask_Goal__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          roomie_msgs__action__PerformTask_Goal__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!roomie_msgs__action__PerformTask_Goal__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `message`
// already included above
// #include "rosidl_runtime_c/string_functions.h"

bool
roomie_msgs__action__PerformTask_Result__init(roomie_msgs__action__PerformTask_Result * msg)
{
  if (!msg) {
    return false;
  }
  // robot_id
  // task_id
  // success
  // message
  if (!rosidl_runtime_c__String__init(&msg->message)) {
    roomie_msgs__action__PerformTask_Result__fini(msg);
    return false;
  }
  return true;
}

void
roomie_msgs__action__PerformTask_Result__fini(roomie_msgs__action__PerformTask_Result * msg)
{
  if (!msg) {
    return;
  }
  // robot_id
  // task_id
  // success
  // message
  rosidl_runtime_c__String__fini(&msg->message);
}

bool
roomie_msgs__action__PerformTask_Result__are_equal(const roomie_msgs__action__PerformTask_Result * lhs, const roomie_msgs__action__PerformTask_Result * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // robot_id
  if (lhs->robot_id != rhs->robot_id) {
    return false;
  }
  // task_id
  if (lhs->task_id != rhs->task_id) {
    return false;
  }
  // success
  if (lhs->success != rhs->success) {
    return false;
  }
  // message
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->message), &(rhs->message)))
  {
    return false;
  }
  return true;
}

bool
roomie_msgs__action__PerformTask_Result__copy(
  const roomie_msgs__action__PerformTask_Result * input,
  roomie_msgs__action__PerformTask_Result * output)
{
  if (!input || !output) {
    return false;
  }
  // robot_id
  output->robot_id = input->robot_id;
  // task_id
  output->task_id = input->task_id;
  // success
  output->success = input->success;
  // message
  if (!rosidl_runtime_c__String__copy(
      &(input->message), &(output->message)))
  {
    return false;
  }
  return true;
}

roomie_msgs__action__PerformTask_Result *
roomie_msgs__action__PerformTask_Result__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  roomie_msgs__action__PerformTask_Result * msg = (roomie_msgs__action__PerformTask_Result *)allocator.allocate(sizeof(roomie_msgs__action__PerformTask_Result), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(roomie_msgs__action__PerformTask_Result));
  bool success = roomie_msgs__action__PerformTask_Result__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
roomie_msgs__action__PerformTask_Result__destroy(roomie_msgs__action__PerformTask_Result * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    roomie_msgs__action__PerformTask_Result__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
roomie_msgs__action__PerformTask_Result__Sequence__init(roomie_msgs__action__PerformTask_Result__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  roomie_msgs__action__PerformTask_Result * data = NULL;

  if (size) {
    data = (roomie_msgs__action__PerformTask_Result *)allocator.zero_allocate(size, sizeof(roomie_msgs__action__PerformTask_Result), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = roomie_msgs__action__PerformTask_Result__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        roomie_msgs__action__PerformTask_Result__fini(&data[i - 1]);
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
roomie_msgs__action__PerformTask_Result__Sequence__fini(roomie_msgs__action__PerformTask_Result__Sequence * array)
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
      roomie_msgs__action__PerformTask_Result__fini(&array->data[i]);
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

roomie_msgs__action__PerformTask_Result__Sequence *
roomie_msgs__action__PerformTask_Result__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  roomie_msgs__action__PerformTask_Result__Sequence * array = (roomie_msgs__action__PerformTask_Result__Sequence *)allocator.allocate(sizeof(roomie_msgs__action__PerformTask_Result__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = roomie_msgs__action__PerformTask_Result__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
roomie_msgs__action__PerformTask_Result__Sequence__destroy(roomie_msgs__action__PerformTask_Result__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    roomie_msgs__action__PerformTask_Result__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
roomie_msgs__action__PerformTask_Result__Sequence__are_equal(const roomie_msgs__action__PerformTask_Result__Sequence * lhs, const roomie_msgs__action__PerformTask_Result__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!roomie_msgs__action__PerformTask_Result__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
roomie_msgs__action__PerformTask_Result__Sequence__copy(
  const roomie_msgs__action__PerformTask_Result__Sequence * input,
  roomie_msgs__action__PerformTask_Result__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(roomie_msgs__action__PerformTask_Result);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    roomie_msgs__action__PerformTask_Result * data =
      (roomie_msgs__action__PerformTask_Result *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!roomie_msgs__action__PerformTask_Result__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          roomie_msgs__action__PerformTask_Result__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!roomie_msgs__action__PerformTask_Result__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


bool
roomie_msgs__action__PerformTask_Feedback__init(roomie_msgs__action__PerformTask_Feedback * msg)
{
  if (!msg) {
    return false;
  }
  // robot_id
  // task_id
  // task_status_id
  return true;
}

void
roomie_msgs__action__PerformTask_Feedback__fini(roomie_msgs__action__PerformTask_Feedback * msg)
{
  if (!msg) {
    return;
  }
  // robot_id
  // task_id
  // task_status_id
}

bool
roomie_msgs__action__PerformTask_Feedback__are_equal(const roomie_msgs__action__PerformTask_Feedback * lhs, const roomie_msgs__action__PerformTask_Feedback * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // robot_id
  if (lhs->robot_id != rhs->robot_id) {
    return false;
  }
  // task_id
  if (lhs->task_id != rhs->task_id) {
    return false;
  }
  // task_status_id
  if (lhs->task_status_id != rhs->task_status_id) {
    return false;
  }
  return true;
}

bool
roomie_msgs__action__PerformTask_Feedback__copy(
  const roomie_msgs__action__PerformTask_Feedback * input,
  roomie_msgs__action__PerformTask_Feedback * output)
{
  if (!input || !output) {
    return false;
  }
  // robot_id
  output->robot_id = input->robot_id;
  // task_id
  output->task_id = input->task_id;
  // task_status_id
  output->task_status_id = input->task_status_id;
  return true;
}

roomie_msgs__action__PerformTask_Feedback *
roomie_msgs__action__PerformTask_Feedback__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  roomie_msgs__action__PerformTask_Feedback * msg = (roomie_msgs__action__PerformTask_Feedback *)allocator.allocate(sizeof(roomie_msgs__action__PerformTask_Feedback), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(roomie_msgs__action__PerformTask_Feedback));
  bool success = roomie_msgs__action__PerformTask_Feedback__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
roomie_msgs__action__PerformTask_Feedback__destroy(roomie_msgs__action__PerformTask_Feedback * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    roomie_msgs__action__PerformTask_Feedback__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
roomie_msgs__action__PerformTask_Feedback__Sequence__init(roomie_msgs__action__PerformTask_Feedback__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  roomie_msgs__action__PerformTask_Feedback * data = NULL;

  if (size) {
    data = (roomie_msgs__action__PerformTask_Feedback *)allocator.zero_allocate(size, sizeof(roomie_msgs__action__PerformTask_Feedback), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = roomie_msgs__action__PerformTask_Feedback__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        roomie_msgs__action__PerformTask_Feedback__fini(&data[i - 1]);
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
roomie_msgs__action__PerformTask_Feedback__Sequence__fini(roomie_msgs__action__PerformTask_Feedback__Sequence * array)
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
      roomie_msgs__action__PerformTask_Feedback__fini(&array->data[i]);
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

roomie_msgs__action__PerformTask_Feedback__Sequence *
roomie_msgs__action__PerformTask_Feedback__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  roomie_msgs__action__PerformTask_Feedback__Sequence * array = (roomie_msgs__action__PerformTask_Feedback__Sequence *)allocator.allocate(sizeof(roomie_msgs__action__PerformTask_Feedback__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = roomie_msgs__action__PerformTask_Feedback__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
roomie_msgs__action__PerformTask_Feedback__Sequence__destroy(roomie_msgs__action__PerformTask_Feedback__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    roomie_msgs__action__PerformTask_Feedback__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
roomie_msgs__action__PerformTask_Feedback__Sequence__are_equal(const roomie_msgs__action__PerformTask_Feedback__Sequence * lhs, const roomie_msgs__action__PerformTask_Feedback__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!roomie_msgs__action__PerformTask_Feedback__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
roomie_msgs__action__PerformTask_Feedback__Sequence__copy(
  const roomie_msgs__action__PerformTask_Feedback__Sequence * input,
  roomie_msgs__action__PerformTask_Feedback__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(roomie_msgs__action__PerformTask_Feedback);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    roomie_msgs__action__PerformTask_Feedback * data =
      (roomie_msgs__action__PerformTask_Feedback *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!roomie_msgs__action__PerformTask_Feedback__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          roomie_msgs__action__PerformTask_Feedback__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!roomie_msgs__action__PerformTask_Feedback__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `goal_id`
#include "unique_identifier_msgs/msg/detail/uuid__functions.h"
// Member `goal`
// already included above
// #include "roomie_msgs/action/detail/perform_task__functions.h"

bool
roomie_msgs__action__PerformTask_SendGoal_Request__init(roomie_msgs__action__PerformTask_SendGoal_Request * msg)
{
  if (!msg) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__init(&msg->goal_id)) {
    roomie_msgs__action__PerformTask_SendGoal_Request__fini(msg);
    return false;
  }
  // goal
  if (!roomie_msgs__action__PerformTask_Goal__init(&msg->goal)) {
    roomie_msgs__action__PerformTask_SendGoal_Request__fini(msg);
    return false;
  }
  return true;
}

void
roomie_msgs__action__PerformTask_SendGoal_Request__fini(roomie_msgs__action__PerformTask_SendGoal_Request * msg)
{
  if (!msg) {
    return;
  }
  // goal_id
  unique_identifier_msgs__msg__UUID__fini(&msg->goal_id);
  // goal
  roomie_msgs__action__PerformTask_Goal__fini(&msg->goal);
}

bool
roomie_msgs__action__PerformTask_SendGoal_Request__are_equal(const roomie_msgs__action__PerformTask_SendGoal_Request * lhs, const roomie_msgs__action__PerformTask_SendGoal_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__are_equal(
      &(lhs->goal_id), &(rhs->goal_id)))
  {
    return false;
  }
  // goal
  if (!roomie_msgs__action__PerformTask_Goal__are_equal(
      &(lhs->goal), &(rhs->goal)))
  {
    return false;
  }
  return true;
}

bool
roomie_msgs__action__PerformTask_SendGoal_Request__copy(
  const roomie_msgs__action__PerformTask_SendGoal_Request * input,
  roomie_msgs__action__PerformTask_SendGoal_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__copy(
      &(input->goal_id), &(output->goal_id)))
  {
    return false;
  }
  // goal
  if (!roomie_msgs__action__PerformTask_Goal__copy(
      &(input->goal), &(output->goal)))
  {
    return false;
  }
  return true;
}

roomie_msgs__action__PerformTask_SendGoal_Request *
roomie_msgs__action__PerformTask_SendGoal_Request__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  roomie_msgs__action__PerformTask_SendGoal_Request * msg = (roomie_msgs__action__PerformTask_SendGoal_Request *)allocator.allocate(sizeof(roomie_msgs__action__PerformTask_SendGoal_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(roomie_msgs__action__PerformTask_SendGoal_Request));
  bool success = roomie_msgs__action__PerformTask_SendGoal_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
roomie_msgs__action__PerformTask_SendGoal_Request__destroy(roomie_msgs__action__PerformTask_SendGoal_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    roomie_msgs__action__PerformTask_SendGoal_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
roomie_msgs__action__PerformTask_SendGoal_Request__Sequence__init(roomie_msgs__action__PerformTask_SendGoal_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  roomie_msgs__action__PerformTask_SendGoal_Request * data = NULL;

  if (size) {
    data = (roomie_msgs__action__PerformTask_SendGoal_Request *)allocator.zero_allocate(size, sizeof(roomie_msgs__action__PerformTask_SendGoal_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = roomie_msgs__action__PerformTask_SendGoal_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        roomie_msgs__action__PerformTask_SendGoal_Request__fini(&data[i - 1]);
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
roomie_msgs__action__PerformTask_SendGoal_Request__Sequence__fini(roomie_msgs__action__PerformTask_SendGoal_Request__Sequence * array)
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
      roomie_msgs__action__PerformTask_SendGoal_Request__fini(&array->data[i]);
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

roomie_msgs__action__PerformTask_SendGoal_Request__Sequence *
roomie_msgs__action__PerformTask_SendGoal_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  roomie_msgs__action__PerformTask_SendGoal_Request__Sequence * array = (roomie_msgs__action__PerformTask_SendGoal_Request__Sequence *)allocator.allocate(sizeof(roomie_msgs__action__PerformTask_SendGoal_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = roomie_msgs__action__PerformTask_SendGoal_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
roomie_msgs__action__PerformTask_SendGoal_Request__Sequence__destroy(roomie_msgs__action__PerformTask_SendGoal_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    roomie_msgs__action__PerformTask_SendGoal_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
roomie_msgs__action__PerformTask_SendGoal_Request__Sequence__are_equal(const roomie_msgs__action__PerformTask_SendGoal_Request__Sequence * lhs, const roomie_msgs__action__PerformTask_SendGoal_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!roomie_msgs__action__PerformTask_SendGoal_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
roomie_msgs__action__PerformTask_SendGoal_Request__Sequence__copy(
  const roomie_msgs__action__PerformTask_SendGoal_Request__Sequence * input,
  roomie_msgs__action__PerformTask_SendGoal_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(roomie_msgs__action__PerformTask_SendGoal_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    roomie_msgs__action__PerformTask_SendGoal_Request * data =
      (roomie_msgs__action__PerformTask_SendGoal_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!roomie_msgs__action__PerformTask_SendGoal_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          roomie_msgs__action__PerformTask_SendGoal_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!roomie_msgs__action__PerformTask_SendGoal_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `stamp`
#include "builtin_interfaces/msg/detail/time__functions.h"

bool
roomie_msgs__action__PerformTask_SendGoal_Response__init(roomie_msgs__action__PerformTask_SendGoal_Response * msg)
{
  if (!msg) {
    return false;
  }
  // accepted
  // stamp
  if (!builtin_interfaces__msg__Time__init(&msg->stamp)) {
    roomie_msgs__action__PerformTask_SendGoal_Response__fini(msg);
    return false;
  }
  return true;
}

void
roomie_msgs__action__PerformTask_SendGoal_Response__fini(roomie_msgs__action__PerformTask_SendGoal_Response * msg)
{
  if (!msg) {
    return;
  }
  // accepted
  // stamp
  builtin_interfaces__msg__Time__fini(&msg->stamp);
}

bool
roomie_msgs__action__PerformTask_SendGoal_Response__are_equal(const roomie_msgs__action__PerformTask_SendGoal_Response * lhs, const roomie_msgs__action__PerformTask_SendGoal_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // accepted
  if (lhs->accepted != rhs->accepted) {
    return false;
  }
  // stamp
  if (!builtin_interfaces__msg__Time__are_equal(
      &(lhs->stamp), &(rhs->stamp)))
  {
    return false;
  }
  return true;
}

bool
roomie_msgs__action__PerformTask_SendGoal_Response__copy(
  const roomie_msgs__action__PerformTask_SendGoal_Response * input,
  roomie_msgs__action__PerformTask_SendGoal_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // accepted
  output->accepted = input->accepted;
  // stamp
  if (!builtin_interfaces__msg__Time__copy(
      &(input->stamp), &(output->stamp)))
  {
    return false;
  }
  return true;
}

roomie_msgs__action__PerformTask_SendGoal_Response *
roomie_msgs__action__PerformTask_SendGoal_Response__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  roomie_msgs__action__PerformTask_SendGoal_Response * msg = (roomie_msgs__action__PerformTask_SendGoal_Response *)allocator.allocate(sizeof(roomie_msgs__action__PerformTask_SendGoal_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(roomie_msgs__action__PerformTask_SendGoal_Response));
  bool success = roomie_msgs__action__PerformTask_SendGoal_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
roomie_msgs__action__PerformTask_SendGoal_Response__destroy(roomie_msgs__action__PerformTask_SendGoal_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    roomie_msgs__action__PerformTask_SendGoal_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
roomie_msgs__action__PerformTask_SendGoal_Response__Sequence__init(roomie_msgs__action__PerformTask_SendGoal_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  roomie_msgs__action__PerformTask_SendGoal_Response * data = NULL;

  if (size) {
    data = (roomie_msgs__action__PerformTask_SendGoal_Response *)allocator.zero_allocate(size, sizeof(roomie_msgs__action__PerformTask_SendGoal_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = roomie_msgs__action__PerformTask_SendGoal_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        roomie_msgs__action__PerformTask_SendGoal_Response__fini(&data[i - 1]);
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
roomie_msgs__action__PerformTask_SendGoal_Response__Sequence__fini(roomie_msgs__action__PerformTask_SendGoal_Response__Sequence * array)
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
      roomie_msgs__action__PerformTask_SendGoal_Response__fini(&array->data[i]);
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

roomie_msgs__action__PerformTask_SendGoal_Response__Sequence *
roomie_msgs__action__PerformTask_SendGoal_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  roomie_msgs__action__PerformTask_SendGoal_Response__Sequence * array = (roomie_msgs__action__PerformTask_SendGoal_Response__Sequence *)allocator.allocate(sizeof(roomie_msgs__action__PerformTask_SendGoal_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = roomie_msgs__action__PerformTask_SendGoal_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
roomie_msgs__action__PerformTask_SendGoal_Response__Sequence__destroy(roomie_msgs__action__PerformTask_SendGoal_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    roomie_msgs__action__PerformTask_SendGoal_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
roomie_msgs__action__PerformTask_SendGoal_Response__Sequence__are_equal(const roomie_msgs__action__PerformTask_SendGoal_Response__Sequence * lhs, const roomie_msgs__action__PerformTask_SendGoal_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!roomie_msgs__action__PerformTask_SendGoal_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
roomie_msgs__action__PerformTask_SendGoal_Response__Sequence__copy(
  const roomie_msgs__action__PerformTask_SendGoal_Response__Sequence * input,
  roomie_msgs__action__PerformTask_SendGoal_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(roomie_msgs__action__PerformTask_SendGoal_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    roomie_msgs__action__PerformTask_SendGoal_Response * data =
      (roomie_msgs__action__PerformTask_SendGoal_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!roomie_msgs__action__PerformTask_SendGoal_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          roomie_msgs__action__PerformTask_SendGoal_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!roomie_msgs__action__PerformTask_SendGoal_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `info`
#include "service_msgs/msg/detail/service_event_info__functions.h"
// Member `request`
// Member `response`
// already included above
// #include "roomie_msgs/action/detail/perform_task__functions.h"

bool
roomie_msgs__action__PerformTask_SendGoal_Event__init(roomie_msgs__action__PerformTask_SendGoal_Event * msg)
{
  if (!msg) {
    return false;
  }
  // info
  if (!service_msgs__msg__ServiceEventInfo__init(&msg->info)) {
    roomie_msgs__action__PerformTask_SendGoal_Event__fini(msg);
    return false;
  }
  // request
  if (!roomie_msgs__action__PerformTask_SendGoal_Request__Sequence__init(&msg->request, 0)) {
    roomie_msgs__action__PerformTask_SendGoal_Event__fini(msg);
    return false;
  }
  // response
  if (!roomie_msgs__action__PerformTask_SendGoal_Response__Sequence__init(&msg->response, 0)) {
    roomie_msgs__action__PerformTask_SendGoal_Event__fini(msg);
    return false;
  }
  return true;
}

void
roomie_msgs__action__PerformTask_SendGoal_Event__fini(roomie_msgs__action__PerformTask_SendGoal_Event * msg)
{
  if (!msg) {
    return;
  }
  // info
  service_msgs__msg__ServiceEventInfo__fini(&msg->info);
  // request
  roomie_msgs__action__PerformTask_SendGoal_Request__Sequence__fini(&msg->request);
  // response
  roomie_msgs__action__PerformTask_SendGoal_Response__Sequence__fini(&msg->response);
}

bool
roomie_msgs__action__PerformTask_SendGoal_Event__are_equal(const roomie_msgs__action__PerformTask_SendGoal_Event * lhs, const roomie_msgs__action__PerformTask_SendGoal_Event * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // info
  if (!service_msgs__msg__ServiceEventInfo__are_equal(
      &(lhs->info), &(rhs->info)))
  {
    return false;
  }
  // request
  if (!roomie_msgs__action__PerformTask_SendGoal_Request__Sequence__are_equal(
      &(lhs->request), &(rhs->request)))
  {
    return false;
  }
  // response
  if (!roomie_msgs__action__PerformTask_SendGoal_Response__Sequence__are_equal(
      &(lhs->response), &(rhs->response)))
  {
    return false;
  }
  return true;
}

bool
roomie_msgs__action__PerformTask_SendGoal_Event__copy(
  const roomie_msgs__action__PerformTask_SendGoal_Event * input,
  roomie_msgs__action__PerformTask_SendGoal_Event * output)
{
  if (!input || !output) {
    return false;
  }
  // info
  if (!service_msgs__msg__ServiceEventInfo__copy(
      &(input->info), &(output->info)))
  {
    return false;
  }
  // request
  if (!roomie_msgs__action__PerformTask_SendGoal_Request__Sequence__copy(
      &(input->request), &(output->request)))
  {
    return false;
  }
  // response
  if (!roomie_msgs__action__PerformTask_SendGoal_Response__Sequence__copy(
      &(input->response), &(output->response)))
  {
    return false;
  }
  return true;
}

roomie_msgs__action__PerformTask_SendGoal_Event *
roomie_msgs__action__PerformTask_SendGoal_Event__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  roomie_msgs__action__PerformTask_SendGoal_Event * msg = (roomie_msgs__action__PerformTask_SendGoal_Event *)allocator.allocate(sizeof(roomie_msgs__action__PerformTask_SendGoal_Event), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(roomie_msgs__action__PerformTask_SendGoal_Event));
  bool success = roomie_msgs__action__PerformTask_SendGoal_Event__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
roomie_msgs__action__PerformTask_SendGoal_Event__destroy(roomie_msgs__action__PerformTask_SendGoal_Event * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    roomie_msgs__action__PerformTask_SendGoal_Event__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
roomie_msgs__action__PerformTask_SendGoal_Event__Sequence__init(roomie_msgs__action__PerformTask_SendGoal_Event__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  roomie_msgs__action__PerformTask_SendGoal_Event * data = NULL;

  if (size) {
    data = (roomie_msgs__action__PerformTask_SendGoal_Event *)allocator.zero_allocate(size, sizeof(roomie_msgs__action__PerformTask_SendGoal_Event), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = roomie_msgs__action__PerformTask_SendGoal_Event__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        roomie_msgs__action__PerformTask_SendGoal_Event__fini(&data[i - 1]);
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
roomie_msgs__action__PerformTask_SendGoal_Event__Sequence__fini(roomie_msgs__action__PerformTask_SendGoal_Event__Sequence * array)
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
      roomie_msgs__action__PerformTask_SendGoal_Event__fini(&array->data[i]);
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

roomie_msgs__action__PerformTask_SendGoal_Event__Sequence *
roomie_msgs__action__PerformTask_SendGoal_Event__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  roomie_msgs__action__PerformTask_SendGoal_Event__Sequence * array = (roomie_msgs__action__PerformTask_SendGoal_Event__Sequence *)allocator.allocate(sizeof(roomie_msgs__action__PerformTask_SendGoal_Event__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = roomie_msgs__action__PerformTask_SendGoal_Event__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
roomie_msgs__action__PerformTask_SendGoal_Event__Sequence__destroy(roomie_msgs__action__PerformTask_SendGoal_Event__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    roomie_msgs__action__PerformTask_SendGoal_Event__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
roomie_msgs__action__PerformTask_SendGoal_Event__Sequence__are_equal(const roomie_msgs__action__PerformTask_SendGoal_Event__Sequence * lhs, const roomie_msgs__action__PerformTask_SendGoal_Event__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!roomie_msgs__action__PerformTask_SendGoal_Event__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
roomie_msgs__action__PerformTask_SendGoal_Event__Sequence__copy(
  const roomie_msgs__action__PerformTask_SendGoal_Event__Sequence * input,
  roomie_msgs__action__PerformTask_SendGoal_Event__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(roomie_msgs__action__PerformTask_SendGoal_Event);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    roomie_msgs__action__PerformTask_SendGoal_Event * data =
      (roomie_msgs__action__PerformTask_SendGoal_Event *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!roomie_msgs__action__PerformTask_SendGoal_Event__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          roomie_msgs__action__PerformTask_SendGoal_Event__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!roomie_msgs__action__PerformTask_SendGoal_Event__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `goal_id`
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__functions.h"

bool
roomie_msgs__action__PerformTask_GetResult_Request__init(roomie_msgs__action__PerformTask_GetResult_Request * msg)
{
  if (!msg) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__init(&msg->goal_id)) {
    roomie_msgs__action__PerformTask_GetResult_Request__fini(msg);
    return false;
  }
  return true;
}

void
roomie_msgs__action__PerformTask_GetResult_Request__fini(roomie_msgs__action__PerformTask_GetResult_Request * msg)
{
  if (!msg) {
    return;
  }
  // goal_id
  unique_identifier_msgs__msg__UUID__fini(&msg->goal_id);
}

bool
roomie_msgs__action__PerformTask_GetResult_Request__are_equal(const roomie_msgs__action__PerformTask_GetResult_Request * lhs, const roomie_msgs__action__PerformTask_GetResult_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__are_equal(
      &(lhs->goal_id), &(rhs->goal_id)))
  {
    return false;
  }
  return true;
}

bool
roomie_msgs__action__PerformTask_GetResult_Request__copy(
  const roomie_msgs__action__PerformTask_GetResult_Request * input,
  roomie_msgs__action__PerformTask_GetResult_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__copy(
      &(input->goal_id), &(output->goal_id)))
  {
    return false;
  }
  return true;
}

roomie_msgs__action__PerformTask_GetResult_Request *
roomie_msgs__action__PerformTask_GetResult_Request__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  roomie_msgs__action__PerformTask_GetResult_Request * msg = (roomie_msgs__action__PerformTask_GetResult_Request *)allocator.allocate(sizeof(roomie_msgs__action__PerformTask_GetResult_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(roomie_msgs__action__PerformTask_GetResult_Request));
  bool success = roomie_msgs__action__PerformTask_GetResult_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
roomie_msgs__action__PerformTask_GetResult_Request__destroy(roomie_msgs__action__PerformTask_GetResult_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    roomie_msgs__action__PerformTask_GetResult_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
roomie_msgs__action__PerformTask_GetResult_Request__Sequence__init(roomie_msgs__action__PerformTask_GetResult_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  roomie_msgs__action__PerformTask_GetResult_Request * data = NULL;

  if (size) {
    data = (roomie_msgs__action__PerformTask_GetResult_Request *)allocator.zero_allocate(size, sizeof(roomie_msgs__action__PerformTask_GetResult_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = roomie_msgs__action__PerformTask_GetResult_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        roomie_msgs__action__PerformTask_GetResult_Request__fini(&data[i - 1]);
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
roomie_msgs__action__PerformTask_GetResult_Request__Sequence__fini(roomie_msgs__action__PerformTask_GetResult_Request__Sequence * array)
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
      roomie_msgs__action__PerformTask_GetResult_Request__fini(&array->data[i]);
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

roomie_msgs__action__PerformTask_GetResult_Request__Sequence *
roomie_msgs__action__PerformTask_GetResult_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  roomie_msgs__action__PerformTask_GetResult_Request__Sequence * array = (roomie_msgs__action__PerformTask_GetResult_Request__Sequence *)allocator.allocate(sizeof(roomie_msgs__action__PerformTask_GetResult_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = roomie_msgs__action__PerformTask_GetResult_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
roomie_msgs__action__PerformTask_GetResult_Request__Sequence__destroy(roomie_msgs__action__PerformTask_GetResult_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    roomie_msgs__action__PerformTask_GetResult_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
roomie_msgs__action__PerformTask_GetResult_Request__Sequence__are_equal(const roomie_msgs__action__PerformTask_GetResult_Request__Sequence * lhs, const roomie_msgs__action__PerformTask_GetResult_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!roomie_msgs__action__PerformTask_GetResult_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
roomie_msgs__action__PerformTask_GetResult_Request__Sequence__copy(
  const roomie_msgs__action__PerformTask_GetResult_Request__Sequence * input,
  roomie_msgs__action__PerformTask_GetResult_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(roomie_msgs__action__PerformTask_GetResult_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    roomie_msgs__action__PerformTask_GetResult_Request * data =
      (roomie_msgs__action__PerformTask_GetResult_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!roomie_msgs__action__PerformTask_GetResult_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          roomie_msgs__action__PerformTask_GetResult_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!roomie_msgs__action__PerformTask_GetResult_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `result`
// already included above
// #include "roomie_msgs/action/detail/perform_task__functions.h"

bool
roomie_msgs__action__PerformTask_GetResult_Response__init(roomie_msgs__action__PerformTask_GetResult_Response * msg)
{
  if (!msg) {
    return false;
  }
  // status
  // result
  if (!roomie_msgs__action__PerformTask_Result__init(&msg->result)) {
    roomie_msgs__action__PerformTask_GetResult_Response__fini(msg);
    return false;
  }
  return true;
}

void
roomie_msgs__action__PerformTask_GetResult_Response__fini(roomie_msgs__action__PerformTask_GetResult_Response * msg)
{
  if (!msg) {
    return;
  }
  // status
  // result
  roomie_msgs__action__PerformTask_Result__fini(&msg->result);
}

bool
roomie_msgs__action__PerformTask_GetResult_Response__are_equal(const roomie_msgs__action__PerformTask_GetResult_Response * lhs, const roomie_msgs__action__PerformTask_GetResult_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // status
  if (lhs->status != rhs->status) {
    return false;
  }
  // result
  if (!roomie_msgs__action__PerformTask_Result__are_equal(
      &(lhs->result), &(rhs->result)))
  {
    return false;
  }
  return true;
}

bool
roomie_msgs__action__PerformTask_GetResult_Response__copy(
  const roomie_msgs__action__PerformTask_GetResult_Response * input,
  roomie_msgs__action__PerformTask_GetResult_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // status
  output->status = input->status;
  // result
  if (!roomie_msgs__action__PerformTask_Result__copy(
      &(input->result), &(output->result)))
  {
    return false;
  }
  return true;
}

roomie_msgs__action__PerformTask_GetResult_Response *
roomie_msgs__action__PerformTask_GetResult_Response__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  roomie_msgs__action__PerformTask_GetResult_Response * msg = (roomie_msgs__action__PerformTask_GetResult_Response *)allocator.allocate(sizeof(roomie_msgs__action__PerformTask_GetResult_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(roomie_msgs__action__PerformTask_GetResult_Response));
  bool success = roomie_msgs__action__PerformTask_GetResult_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
roomie_msgs__action__PerformTask_GetResult_Response__destroy(roomie_msgs__action__PerformTask_GetResult_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    roomie_msgs__action__PerformTask_GetResult_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
roomie_msgs__action__PerformTask_GetResult_Response__Sequence__init(roomie_msgs__action__PerformTask_GetResult_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  roomie_msgs__action__PerformTask_GetResult_Response * data = NULL;

  if (size) {
    data = (roomie_msgs__action__PerformTask_GetResult_Response *)allocator.zero_allocate(size, sizeof(roomie_msgs__action__PerformTask_GetResult_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = roomie_msgs__action__PerformTask_GetResult_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        roomie_msgs__action__PerformTask_GetResult_Response__fini(&data[i - 1]);
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
roomie_msgs__action__PerformTask_GetResult_Response__Sequence__fini(roomie_msgs__action__PerformTask_GetResult_Response__Sequence * array)
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
      roomie_msgs__action__PerformTask_GetResult_Response__fini(&array->data[i]);
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

roomie_msgs__action__PerformTask_GetResult_Response__Sequence *
roomie_msgs__action__PerformTask_GetResult_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  roomie_msgs__action__PerformTask_GetResult_Response__Sequence * array = (roomie_msgs__action__PerformTask_GetResult_Response__Sequence *)allocator.allocate(sizeof(roomie_msgs__action__PerformTask_GetResult_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = roomie_msgs__action__PerformTask_GetResult_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
roomie_msgs__action__PerformTask_GetResult_Response__Sequence__destroy(roomie_msgs__action__PerformTask_GetResult_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    roomie_msgs__action__PerformTask_GetResult_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
roomie_msgs__action__PerformTask_GetResult_Response__Sequence__are_equal(const roomie_msgs__action__PerformTask_GetResult_Response__Sequence * lhs, const roomie_msgs__action__PerformTask_GetResult_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!roomie_msgs__action__PerformTask_GetResult_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
roomie_msgs__action__PerformTask_GetResult_Response__Sequence__copy(
  const roomie_msgs__action__PerformTask_GetResult_Response__Sequence * input,
  roomie_msgs__action__PerformTask_GetResult_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(roomie_msgs__action__PerformTask_GetResult_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    roomie_msgs__action__PerformTask_GetResult_Response * data =
      (roomie_msgs__action__PerformTask_GetResult_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!roomie_msgs__action__PerformTask_GetResult_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          roomie_msgs__action__PerformTask_GetResult_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!roomie_msgs__action__PerformTask_GetResult_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `info`
// already included above
// #include "service_msgs/msg/detail/service_event_info__functions.h"
// Member `request`
// Member `response`
// already included above
// #include "roomie_msgs/action/detail/perform_task__functions.h"

bool
roomie_msgs__action__PerformTask_GetResult_Event__init(roomie_msgs__action__PerformTask_GetResult_Event * msg)
{
  if (!msg) {
    return false;
  }
  // info
  if (!service_msgs__msg__ServiceEventInfo__init(&msg->info)) {
    roomie_msgs__action__PerformTask_GetResult_Event__fini(msg);
    return false;
  }
  // request
  if (!roomie_msgs__action__PerformTask_GetResult_Request__Sequence__init(&msg->request, 0)) {
    roomie_msgs__action__PerformTask_GetResult_Event__fini(msg);
    return false;
  }
  // response
  if (!roomie_msgs__action__PerformTask_GetResult_Response__Sequence__init(&msg->response, 0)) {
    roomie_msgs__action__PerformTask_GetResult_Event__fini(msg);
    return false;
  }
  return true;
}

void
roomie_msgs__action__PerformTask_GetResult_Event__fini(roomie_msgs__action__PerformTask_GetResult_Event * msg)
{
  if (!msg) {
    return;
  }
  // info
  service_msgs__msg__ServiceEventInfo__fini(&msg->info);
  // request
  roomie_msgs__action__PerformTask_GetResult_Request__Sequence__fini(&msg->request);
  // response
  roomie_msgs__action__PerformTask_GetResult_Response__Sequence__fini(&msg->response);
}

bool
roomie_msgs__action__PerformTask_GetResult_Event__are_equal(const roomie_msgs__action__PerformTask_GetResult_Event * lhs, const roomie_msgs__action__PerformTask_GetResult_Event * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // info
  if (!service_msgs__msg__ServiceEventInfo__are_equal(
      &(lhs->info), &(rhs->info)))
  {
    return false;
  }
  // request
  if (!roomie_msgs__action__PerformTask_GetResult_Request__Sequence__are_equal(
      &(lhs->request), &(rhs->request)))
  {
    return false;
  }
  // response
  if (!roomie_msgs__action__PerformTask_GetResult_Response__Sequence__are_equal(
      &(lhs->response), &(rhs->response)))
  {
    return false;
  }
  return true;
}

bool
roomie_msgs__action__PerformTask_GetResult_Event__copy(
  const roomie_msgs__action__PerformTask_GetResult_Event * input,
  roomie_msgs__action__PerformTask_GetResult_Event * output)
{
  if (!input || !output) {
    return false;
  }
  // info
  if (!service_msgs__msg__ServiceEventInfo__copy(
      &(input->info), &(output->info)))
  {
    return false;
  }
  // request
  if (!roomie_msgs__action__PerformTask_GetResult_Request__Sequence__copy(
      &(input->request), &(output->request)))
  {
    return false;
  }
  // response
  if (!roomie_msgs__action__PerformTask_GetResult_Response__Sequence__copy(
      &(input->response), &(output->response)))
  {
    return false;
  }
  return true;
}

roomie_msgs__action__PerformTask_GetResult_Event *
roomie_msgs__action__PerformTask_GetResult_Event__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  roomie_msgs__action__PerformTask_GetResult_Event * msg = (roomie_msgs__action__PerformTask_GetResult_Event *)allocator.allocate(sizeof(roomie_msgs__action__PerformTask_GetResult_Event), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(roomie_msgs__action__PerformTask_GetResult_Event));
  bool success = roomie_msgs__action__PerformTask_GetResult_Event__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
roomie_msgs__action__PerformTask_GetResult_Event__destroy(roomie_msgs__action__PerformTask_GetResult_Event * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    roomie_msgs__action__PerformTask_GetResult_Event__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
roomie_msgs__action__PerformTask_GetResult_Event__Sequence__init(roomie_msgs__action__PerformTask_GetResult_Event__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  roomie_msgs__action__PerformTask_GetResult_Event * data = NULL;

  if (size) {
    data = (roomie_msgs__action__PerformTask_GetResult_Event *)allocator.zero_allocate(size, sizeof(roomie_msgs__action__PerformTask_GetResult_Event), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = roomie_msgs__action__PerformTask_GetResult_Event__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        roomie_msgs__action__PerformTask_GetResult_Event__fini(&data[i - 1]);
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
roomie_msgs__action__PerformTask_GetResult_Event__Sequence__fini(roomie_msgs__action__PerformTask_GetResult_Event__Sequence * array)
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
      roomie_msgs__action__PerformTask_GetResult_Event__fini(&array->data[i]);
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

roomie_msgs__action__PerformTask_GetResult_Event__Sequence *
roomie_msgs__action__PerformTask_GetResult_Event__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  roomie_msgs__action__PerformTask_GetResult_Event__Sequence * array = (roomie_msgs__action__PerformTask_GetResult_Event__Sequence *)allocator.allocate(sizeof(roomie_msgs__action__PerformTask_GetResult_Event__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = roomie_msgs__action__PerformTask_GetResult_Event__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
roomie_msgs__action__PerformTask_GetResult_Event__Sequence__destroy(roomie_msgs__action__PerformTask_GetResult_Event__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    roomie_msgs__action__PerformTask_GetResult_Event__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
roomie_msgs__action__PerformTask_GetResult_Event__Sequence__are_equal(const roomie_msgs__action__PerformTask_GetResult_Event__Sequence * lhs, const roomie_msgs__action__PerformTask_GetResult_Event__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!roomie_msgs__action__PerformTask_GetResult_Event__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
roomie_msgs__action__PerformTask_GetResult_Event__Sequence__copy(
  const roomie_msgs__action__PerformTask_GetResult_Event__Sequence * input,
  roomie_msgs__action__PerformTask_GetResult_Event__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(roomie_msgs__action__PerformTask_GetResult_Event);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    roomie_msgs__action__PerformTask_GetResult_Event * data =
      (roomie_msgs__action__PerformTask_GetResult_Event *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!roomie_msgs__action__PerformTask_GetResult_Event__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          roomie_msgs__action__PerformTask_GetResult_Event__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!roomie_msgs__action__PerformTask_GetResult_Event__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `goal_id`
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__functions.h"
// Member `feedback`
// already included above
// #include "roomie_msgs/action/detail/perform_task__functions.h"

bool
roomie_msgs__action__PerformTask_FeedbackMessage__init(roomie_msgs__action__PerformTask_FeedbackMessage * msg)
{
  if (!msg) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__init(&msg->goal_id)) {
    roomie_msgs__action__PerformTask_FeedbackMessage__fini(msg);
    return false;
  }
  // feedback
  if (!roomie_msgs__action__PerformTask_Feedback__init(&msg->feedback)) {
    roomie_msgs__action__PerformTask_FeedbackMessage__fini(msg);
    return false;
  }
  return true;
}

void
roomie_msgs__action__PerformTask_FeedbackMessage__fini(roomie_msgs__action__PerformTask_FeedbackMessage * msg)
{
  if (!msg) {
    return;
  }
  // goal_id
  unique_identifier_msgs__msg__UUID__fini(&msg->goal_id);
  // feedback
  roomie_msgs__action__PerformTask_Feedback__fini(&msg->feedback);
}

bool
roomie_msgs__action__PerformTask_FeedbackMessage__are_equal(const roomie_msgs__action__PerformTask_FeedbackMessage * lhs, const roomie_msgs__action__PerformTask_FeedbackMessage * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__are_equal(
      &(lhs->goal_id), &(rhs->goal_id)))
  {
    return false;
  }
  // feedback
  if (!roomie_msgs__action__PerformTask_Feedback__are_equal(
      &(lhs->feedback), &(rhs->feedback)))
  {
    return false;
  }
  return true;
}

bool
roomie_msgs__action__PerformTask_FeedbackMessage__copy(
  const roomie_msgs__action__PerformTask_FeedbackMessage * input,
  roomie_msgs__action__PerformTask_FeedbackMessage * output)
{
  if (!input || !output) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__copy(
      &(input->goal_id), &(output->goal_id)))
  {
    return false;
  }
  // feedback
  if (!roomie_msgs__action__PerformTask_Feedback__copy(
      &(input->feedback), &(output->feedback)))
  {
    return false;
  }
  return true;
}

roomie_msgs__action__PerformTask_FeedbackMessage *
roomie_msgs__action__PerformTask_FeedbackMessage__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  roomie_msgs__action__PerformTask_FeedbackMessage * msg = (roomie_msgs__action__PerformTask_FeedbackMessage *)allocator.allocate(sizeof(roomie_msgs__action__PerformTask_FeedbackMessage), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(roomie_msgs__action__PerformTask_FeedbackMessage));
  bool success = roomie_msgs__action__PerformTask_FeedbackMessage__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
roomie_msgs__action__PerformTask_FeedbackMessage__destroy(roomie_msgs__action__PerformTask_FeedbackMessage * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    roomie_msgs__action__PerformTask_FeedbackMessage__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
roomie_msgs__action__PerformTask_FeedbackMessage__Sequence__init(roomie_msgs__action__PerformTask_FeedbackMessage__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  roomie_msgs__action__PerformTask_FeedbackMessage * data = NULL;

  if (size) {
    data = (roomie_msgs__action__PerformTask_FeedbackMessage *)allocator.zero_allocate(size, sizeof(roomie_msgs__action__PerformTask_FeedbackMessage), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = roomie_msgs__action__PerformTask_FeedbackMessage__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        roomie_msgs__action__PerformTask_FeedbackMessage__fini(&data[i - 1]);
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
roomie_msgs__action__PerformTask_FeedbackMessage__Sequence__fini(roomie_msgs__action__PerformTask_FeedbackMessage__Sequence * array)
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
      roomie_msgs__action__PerformTask_FeedbackMessage__fini(&array->data[i]);
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

roomie_msgs__action__PerformTask_FeedbackMessage__Sequence *
roomie_msgs__action__PerformTask_FeedbackMessage__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  roomie_msgs__action__PerformTask_FeedbackMessage__Sequence * array = (roomie_msgs__action__PerformTask_FeedbackMessage__Sequence *)allocator.allocate(sizeof(roomie_msgs__action__PerformTask_FeedbackMessage__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = roomie_msgs__action__PerformTask_FeedbackMessage__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
roomie_msgs__action__PerformTask_FeedbackMessage__Sequence__destroy(roomie_msgs__action__PerformTask_FeedbackMessage__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    roomie_msgs__action__PerformTask_FeedbackMessage__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
roomie_msgs__action__PerformTask_FeedbackMessage__Sequence__are_equal(const roomie_msgs__action__PerformTask_FeedbackMessage__Sequence * lhs, const roomie_msgs__action__PerformTask_FeedbackMessage__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!roomie_msgs__action__PerformTask_FeedbackMessage__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
roomie_msgs__action__PerformTask_FeedbackMessage__Sequence__copy(
  const roomie_msgs__action__PerformTask_FeedbackMessage__Sequence * input,
  roomie_msgs__action__PerformTask_FeedbackMessage__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(roomie_msgs__action__PerformTask_FeedbackMessage);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    roomie_msgs__action__PerformTask_FeedbackMessage * data =
      (roomie_msgs__action__PerformTask_FeedbackMessage *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!roomie_msgs__action__PerformTask_FeedbackMessage__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          roomie_msgs__action__PerformTask_FeedbackMessage__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!roomie_msgs__action__PerformTask_FeedbackMessage__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
