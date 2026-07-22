---
name: delete-completed-tasks
description: "Delete tasks once they're complete (TaskUpdate status=deleted) — the user doesn't want finished tasks lingering in the list"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: cdaa5dd9-6bb0-480c-84f6-52b33171a7b8
---

When a task is finished, **delete it** from the task tracker (`TaskUpdate` with `status: "deleted"`) rather than leaving it marked completed. The user wants the task list to show only open/remaining work — completed tasks lingering in the list (e.g. "12 tasks (6 done, 6 open)") is clutter they don't want to see.

**Why:** the finished work is already recorded elsewhere (the changelog in `cf/client/docks/changelog.txt` and the Finished section of `cf/client/docks/todo list.txt`), so the tracker doesn't need a permanent done-list — it's a live to-do, not a history.

**How to apply:** mark a task `completed` while wrapping up if you like, but then delete it so only pending/in-progress tasks remain. Keep the changelog and [[changelog-rules]] todo list as the durable record of what shipped.
