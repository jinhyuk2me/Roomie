// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from roomie_msgs:msg/RobotGuiEvent.idl
// generated code does not contain a copyright notice

#include "roomie_msgs/msg/detail/robot_gui_event__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_roomie_msgs
const rosidl_type_hash_t *
roomie_msgs__msg__RobotGuiEvent__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x52, 0xcb, 0x46, 0x2c, 0x70, 0xf7, 0x74, 0xdb,
      0x77, 0xbf, 0x02, 0x34, 0xa1, 0x70, 0x67, 0xda,
      0xf0, 0xad, 0xf7, 0x88, 0x71, 0x94, 0xa3, 0xd1,
      0x59, 0xb7, 0x6b, 0x48, 0x2e, 0x54, 0x4e, 0xe6,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types
#include "builtin_interfaces/msg/detail/time__functions.h"

// Hashes for external referenced types
#ifndef NDEBUG
static const rosidl_type_hash_t builtin_interfaces__msg__Time__EXPECTED_HASH = {1, {
    0xb1, 0x06, 0x23, 0x5e, 0x25, 0xa4, 0xc5, 0xed,
    0x35, 0x09, 0x8a, 0xa0, 0xa6, 0x1a, 0x3e, 0xe9,
    0xc9, 0xb1, 0x8d, 0x19, 0x7f, 0x39, 0x8b, 0x0e,
    0x42, 0x06, 0xce, 0xa9, 0xac, 0xf9, 0xc1, 0x97,
  }};
#endif

static char roomie_msgs__msg__RobotGuiEvent__TYPE_NAME[] = "roomie_msgs/msg/RobotGuiEvent";
static char builtin_interfaces__msg__Time__TYPE_NAME[] = "builtin_interfaces/msg/Time";

// Define type names, field names, and default values
static char roomie_msgs__msg__RobotGuiEvent__FIELD_NAME__robot_id[] = "robot_id";
static char roomie_msgs__msg__RobotGuiEvent__FIELD_NAME__rgui_event_id[] = "rgui_event_id";
static char roomie_msgs__msg__RobotGuiEvent__FIELD_NAME__task_id[] = "task_id";
static char roomie_msgs__msg__RobotGuiEvent__FIELD_NAME__timestamp[] = "timestamp";
static char roomie_msgs__msg__RobotGuiEvent__FIELD_NAME__detail[] = "detail";

static rosidl_runtime_c__type_description__Field roomie_msgs__msg__RobotGuiEvent__FIELDS[] = {
  {
    {roomie_msgs__msg__RobotGuiEvent__FIELD_NAME__robot_id, 8, 8},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_INT32,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {roomie_msgs__msg__RobotGuiEvent__FIELD_NAME__rgui_event_id, 13, 13},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_INT32,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {roomie_msgs__msg__RobotGuiEvent__FIELD_NAME__task_id, 7, 7},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_INT32,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {roomie_msgs__msg__RobotGuiEvent__FIELD_NAME__timestamp, 9, 9},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {builtin_interfaces__msg__Time__TYPE_NAME, 27, 27},
    },
    {NULL, 0, 0},
  },
  {
    {roomie_msgs__msg__RobotGuiEvent__FIELD_NAME__detail, 6, 6},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_STRING,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

static rosidl_runtime_c__type_description__IndividualTypeDescription roomie_msgs__msg__RobotGuiEvent__REFERENCED_TYPE_DESCRIPTIONS[] = {
  {
    {builtin_interfaces__msg__Time__TYPE_NAME, 27, 27},
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
roomie_msgs__msg__RobotGuiEvent__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {roomie_msgs__msg__RobotGuiEvent__TYPE_NAME, 29, 29},
      {roomie_msgs__msg__RobotGuiEvent__FIELDS, 5, 5},
    },
    {roomie_msgs__msg__RobotGuiEvent__REFERENCED_TYPE_DESCRIPTIONS, 1, 1},
  };
  if (!constructed) {
    assert(0 == memcmp(&builtin_interfaces__msg__Time__EXPECTED_HASH, builtin_interfaces__msg__Time__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[0].fields = builtin_interfaces__msg__Time__get_type_description(NULL)->type_description.fields;
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "# RobotGuiEvent.msg\n"
  "int32 robot_id\n"
  "int32 rgui_event_id\n"
  "int32 task_id\n"
  "builtin_interfaces/Time timestamp\n"
  "string detail\n"
  "\n"
  "# rgui_event_id values:\n"
  "# 1: \\xec\\x97\\x98\\xeb\\xa6\\xac\\xeb\\xb2\\xa0\\xec\\x9d\\xb4\\xed\\x84\\xb0 \\xeb\\xb2\\x84\\xed\\x8a\\xbc \\xec\\xa1\\xb0\\xec\\x9e\\x91 \\xec\\x8b\\x9c\\xec\\x9e\\x91\n"
  "# 2: \\xec\\x97\\x98\\xeb\\xa6\\xac\\xeb\\xb2\\xa0\\xec\\x9d\\xb4\\xed\\x84\\xb0 \\xeb\\xb2\\x84\\xed\\x8a\\xbc \\xec\\xa1\\xb0\\xec\\x9e\\x91 \\xec\\xa2\\x85\\xeb\\xa3\\x8c\n"
  "# 3: \\xec\\x97\\x98\\xeb\\xa6\\xac\\xeb\\xb2\\xa0\\xec\\x9d\\xb4\\xed\\x84\\xb0 \\xed\\x83\\x91\\xec\\x8a\\xb9 \\xec\\x8b\\x9c\\xec\\x9e\\x91\n"
  "# 4: \\xec\\x97\\x98\\xeb\\xa6\\xac\\xeb\\xb2\\xa0\\xec\\x9d\\xb4\\xed\\x84\\xb0 \\xed\\x83\\x91\\xec\\x8a\\xb9 \\xec\\xa2\\x85\\xeb\\xa3\\x8c\n"
  "# 5: \\xec\\x97\\x98\\xeb\\xa6\\xac\\xeb\\xb2\\xa0\\xec\\x9d\\xb4\\xed\\x84\\xb0 \\xed\\x95\\x98\\xec\\xb0\\xa8 \\xec\\x8b\\x9c\\xec\\x9e\\x91\n"
  "# 6: \\xec\\x97\\x98\\xeb\\xa6\\xac\\xeb\\xb2\\xa0\\xec\\x9d\\xb4\\xed\\x84\\xb0 \\xed\\x95\\x98\\xec\\xb0\\xa8 \\xec\\xa2\\x85\\xeb\\xa3\\x8c\n"
  "# 7: \\xed\\x98\\xb8\\xec\\xb6\\x9c \\xec\\x9d\\xb4\\xeb\\x8f\\x99 \\xec\\x8b\\x9c\\xec\\x9e\\x91\n"
  "# 8: \\xed\\x98\\xb8\\xec\\xb6\\x9c \\xec\\x9d\\xb4\\xeb\\x8f\\x99 \\xec\\xa2\\x85\\xeb\\xa3\\x8c\n"
  "# 9: \\xed\\x98\\xb8\\xec\\x8b\\xa4 \\xeb\\xb2\\x88\\xed\\x98\\xb8 \\xec\\x9d\\xb8\\xec\\x8b\\x9d \\xec\\x99\\x84\\xeb\\xa3\\x8c\n"
  "# 10: \\xea\\xb8\\xb8\\xec\\x95\\x88\\xeb\\x82\\xb4 \\xec\\x9d\\xb4\\xeb\\x8f\\x99 \\xec\\x8b\\x9c\\xec\\x9e\\x91\n"
  "# 11: \\xea\\xb8\\xb8\\xec\\x95\\x88\\xeb\\x82\\xb4 \\xec\\x9d\\xb4\\xeb\\x8f\\x99 \\xec\\xa2\\x85\\xeb\\xa3\\x8c\n"
  "# 12: \\xed\\x94\\xbd\\xec\\x97\\x85\\xec\\x9e\\xa5\\xec\\x86\\x8c \\xec\\x9d\\xb4\\xeb\\x8f\\x99 \\xec\\x8b\\x9c\\xec\\x9e\\x91\n"
  "# 13: \\xed\\x94\\xbd\\xec\\x97\\x85\\xec\\x9e\\xa5\\xec\\x86\\x8c \\xec\\x9d\\xb4\\xeb\\x8f\\x99 \\xec\\xa2\\x85\\xeb\\xa3\\x8c\n"
  "# 14: \\xeb\\xb0\\xb0\\xec\\x86\\xa1\\xec\\x9e\\xa5\\xec\\x86\\x8c \\xec\\x9d\\xb4\\xeb\\x8f\\x99 \\xec\\x8b\\x9c\\xec\\x9e\\x91 \n"
  "# 15: \\xeb\\xb0\\xb0\\xec\\x86\\xa1\\xec\\x9e\\xa5\\xec\\x86\\x8c \\xeb\\x8f\\x84\\xec\\xb0\\xa9 \\xec\\x99\\x84\\xeb\\xa3\\x8c\n"
  "# 16: \\xec\\x84\\x9c\\xeb\\x9e\\x8d \\xec\\x97\\xb4\\xeb\\xa6\\xbc\n"
  "# 17: \\xec\\x84\\x9c\\xeb\\x9e\\x8d \\xeb\\x8b\\xab\\xed\\x9e\\x98\n"
  "# 18: \\xec\\x84\\x9c\\xeb\\x9e\\x8d \\xec\\x9e\\xa0\\xea\\xb8\\x88\n"
  "# 19: \\xec\\xb6\\xa9\\xec\\xa0\\x84 \\xec\\x8b\\x9c\\xec\\x9e\\x91\n"
  "# 20: \\xec\\xb6\\xa9\\xec\\xa0\\x84 \\xec\\xa2\\x85\\xeb\\xa3\\x8c\n"
  "# 21: \\xed\\x88\\xac\\xec\\x88\\x99\\xea\\xb0\\x9d \\xec\\x9d\\xb4\\xed\\x83\\x88\n"
  "# 22: \\xed\\x88\\xac\\xec\\x88\\x99\\xea\\xb0\\x9d \\xec\\x9d\\xb4\\xed\\x83\\x88 \\xed\\x9b\\x84 \\xec\\x9e\\xac\\xeb\\x93\\xb1\\xeb\\xa1\\x9d\n"
  "# 23: \\xed\\x88\\xac\\xec\\x88\\x99\\xea\\xb0\\x9d \\xeb\\x93\\xb1\\xeb\\xa1\\x9d\n"
  "# 24: \\xeb\\xb0\\xb0\\xec\\x86\\xa1 \\xec\\x88\\x98\\xeb\\xa0\\xb9 \\xec\\x99\\x84\\xeb\\xa3\\x8c\n"
  "# 25: \\xeb\\xb0\\xb0\\xec\\x86\\xa1 \\xec\\x88\\x98\\xeb\\xa0\\xb9 \\xeb\\xaf\\xb8\\xec\\x99\\x84\\xeb\\xa3\\x8c\n"
  "# 100: [\\xec\\x88\\x98\\xeb\\xa0\\xb9 \\xec\\x99\\x84\\xeb\\xa3\\x8c] \\xed\\x81\\xb4\\xeb\\xa6\\xad\n"
  "# 101: \\xeb\\xaa\\xa9\\xec\\xa0\\x81\\xec\\xa7\\x80 \\xec\\x9e\\x85\\xeb\\xa0\\xa5 \\xec\\x99\\x84\\xeb\\xa3\\x8c\n"
  "# 102: \\xec\\x82\\xac\\xec\\x9a\\xa9\\xec\\x9e\\x90 \\xec\\xa0\\x90\\xec\\x9c\\xa0 \\xec\\x83\\x81\\xed\\x83\\x9c\n"
  "# 103: [\\xec\\xb9\\xb4\\xeb\\x93\\x9c\\xed\\x82\\xa4\\xeb\\xa1\\x9c \\xec\\x9e\\x85\\xeb\\xa0\\xa5] \\xec\\x84\\xa0\\xed\\x83\\x9d\n"
  "# 104: [\\xec\\x84\\x9c\\xeb\\x9e\\x8d \\xec\\x97\\xb4\\xea\\xb8\\xb0] \\xed\\x81\\xb4\\xeb\\xa6\\xad\n"
  "# 105: [\\xec\\xa0\\x81\\xec\\x9e\\xac \\xec\\x99\\x84\\xeb\\xa3\\x8c] \\xed\\x81\\xb4\\xeb\\xa6\\xad\n"
  "# 106: \\xec\\x9d\\xb8\\xec\\x8b\\x9d\\xeb\\xaa\\xa8\\xeb\\x93\\x9c \\xec\\xa0\\x84\\xed\\x99\\x98 \\xec\\x9a\\x94\\xec\\xb2\\xad ";

static char msg_encoding[] = "msg";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
roomie_msgs__msg__RobotGuiEvent__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {roomie_msgs__msg__RobotGuiEvent__TYPE_NAME, 29, 29},
    {msg_encoding, 3, 3},
    {toplevel_type_raw_source, 658, 658},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
roomie_msgs__msg__RobotGuiEvent__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[2];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 2, 2};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *roomie_msgs__msg__RobotGuiEvent__get_individual_type_description_source(NULL),
    sources[1] = *builtin_interfaces__msg__Time__get_individual_type_description_source(NULL);
    constructed = true;
  }
  return &source_sequence;
}
