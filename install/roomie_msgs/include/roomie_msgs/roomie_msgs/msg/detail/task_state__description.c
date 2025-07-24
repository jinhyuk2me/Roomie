// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from roomie_msgs:msg/TaskState.idl
// generated code does not contain a copyright notice

#include "roomie_msgs/msg/detail/task_state__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_roomie_msgs
const rosidl_type_hash_t *
roomie_msgs__msg__TaskState__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x1e, 0x6a, 0x08, 0xfe, 0xaf, 0x60, 0xfa, 0x7c,
      0x34, 0x67, 0x21, 0x49, 0xf4, 0xa9, 0x97, 0xb9,
      0xfe, 0x14, 0xd5, 0xfb, 0xe7, 0x0a, 0x64, 0x21,
      0x2d, 0x10, 0xfc, 0x9a, 0xd4, 0x0b, 0x2f, 0x2e,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types

// Hashes for external referenced types
#ifndef NDEBUG
#endif

static char roomie_msgs__msg__TaskState__TYPE_NAME[] = "roomie_msgs/msg/TaskState";

// Define type names, field names, and default values
static char roomie_msgs__msg__TaskState__FIELD_NAME__task_id[] = "task_id";
static char roomie_msgs__msg__TaskState__FIELD_NAME__task_state_id[] = "task_state_id";

static rosidl_runtime_c__type_description__Field roomie_msgs__msg__TaskState__FIELDS[] = {
  {
    {roomie_msgs__msg__TaskState__FIELD_NAME__task_id, 7, 7},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_INT32,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {roomie_msgs__msg__TaskState__FIELD_NAME__task_state_id, 13, 13},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_INT32,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
roomie_msgs__msg__TaskState__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {roomie_msgs__msg__TaskState__TYPE_NAME, 25, 25},
      {roomie_msgs__msg__TaskState__FIELDS, 2, 2},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "# TaskState.msg\n"
  "int32 task_id\n"
  "int32 task_state_id\n"
  "\n"
  "# task_state_id values:\n"
  "# 0: \\xec\\xa0\\x91\\xec\\x88\\x98\\xeb\\x90\\xa8\n"
  "# 1: \\xec\\xa4\\x80\\xeb\\xb9\\x84 \\xec\\x99\\x84\\xeb\\xa3\\x8c\n"
  "# 2: \\xeb\\xa1\\x9c\\xeb\\xb4\\x87 \\xed\\x95\\xa0\\xeb\\x8b\\xb9\\xeb\\x90\\xa8\n"
  "# 3: \\xed\\x94\\xbd\\xec\\x97\\x85 \\xec\\x9e\\xa5\\xec\\x86\\x8c\\xeb\\xa1\\x9c \\xec\\x9d\\xb4\\xeb\\x8f\\x99\n"
  "# 4: \\xed\\x94\\xbd\\xec\\x97\\x85 \\xeb\\x8c\\x80\\xea\\xb8\\xb0 \\xec\\xa4\\x91\n"
  "# 5: \\xeb\\xb0\\xb0\\xec\\x86\\xa1 \\xec\\xa4\\x91\n"
  "# 6: \\xed\\x94\\xbd\\xec\\x97\\x85 \\xeb\\x8f\\x84\\xec\\xb0\\xa9\n"
  "# 7: \\xec\\x88\\x98\\xeb\\xa0\\xb9 \\xec\\x99\\x84\\xeb\\xa3\\x8c\n"
  "# 10: \\xed\\x98\\xb8\\xec\\xb6\\x9c \\xec\\xa0\\x91\\xec\\x88\\x98\\xeb\\x90\\xa8\n"
  "# 11: \\xed\\x98\\xb8\\xec\\xb6\\x9c \\xeb\\xa1\\x9c\\xeb\\xb4\\x87 \\xed\\x95\\xa0\\xeb\\x8b\\xb9\\xeb\\x90\\xa8\n"
  "# 12: \\xed\\x98\\xb8\\xec\\xb6\\x9c \\xec\\x9d\\xb4\\xeb\\x8f\\x99 \\xec\\xa4\\x91\n"
  "# 13: \\xed\\x98\\xb8\\xec\\xb6\\x9c \\xeb\\x8f\\x84\\xec\\xb0\\xa9\n"
  "# 20: \\xea\\xb8\\xb8\\xec\\x95\\x88\\xeb\\x82\\xb4 \\xec\\xa0\\x91\\xec\\x88\\x98\\xeb\\x90\\xa8\n"
  "# 21: \\xea\\xb8\\xb8\\xec\\x95\\x88\\xeb\\x82\\xb4 \\xec\\xa4\\x91\n"
  "# 21: \\xea\\xb8\\xb8\\xec\\x95\\x88\\xeb\\x82\\xb4 \\xeb\\x8f\\x84\\xec\\xb0\\xa9 ";

static char msg_encoding[] = "msg";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
roomie_msgs__msg__TaskState__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {roomie_msgs__msg__TaskState__TYPE_NAME, 25, 25},
    {msg_encoding, 3, 3},
    {toplevel_type_raw_source, 261, 261},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
roomie_msgs__msg__TaskState__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *roomie_msgs__msg__TaskState__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}
