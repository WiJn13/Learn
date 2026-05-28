const STORAGE_KEY = "homeworkQueue.v1";

const subjects = {
  chinese: { label: "语文", bg: "#fff1f2", border: "#fecdd3" },
  math: { label: "数学", bg: "#eff6ff", border: "#bfdbfe" },
  english: { label: "英语", bg: "#ecfdf5", border: "#bbf7d0" },
};

const defaultChildren = [
  { id: createId(), name: "小朋友1", avatar: "⭐", color: "#ef4444" },
  { id: createId(), name: "小朋友2", avatar: "🌙", color: "#f97316" },
  { id: createId(), name: "小朋友3", avatar: "☀️", color: "#eab308" },
  { id: createId(), name: "小朋友4", avatar: "🍀", color: "#22c55e" },
  { id: createId(), name: "小朋友5", avatar: "💧", color: "#06b6d4" },
  { id: createId(), name: "小朋友6", avatar: "🎈", color: "#3b82f6" },
  { id: createId(), name: "小朋友7", avatar: "🎵", color: "#8b5cf6" },
  { id: createId(), name: "小朋友8", avatar: "🌸", color: "#ec4899" },
];

const state = loadState();

const childrenGrid = document.querySelector("#childrenGrid");
const childrenCount = document.querySelector("#childrenCount");
const queueList = document.querySelector("#queueList");
const queueCount = document.querySelector("#queueCount");
const activeList = document.querySelector("#activeList");
const activeCount = document.querySelector("#activeCount");
const doneList = document.querySelector("#doneList");
const doneCount = document.querySelector("#doneCount");
const currentCall = document.querySelector("#currentCall");
const editorDialog = document.querySelector("#editorDialog");
const editorList = document.querySelector("#editorList");

document.querySelector("#nextButton").addEventListener("click", callNext);
document.querySelector("#replayButton").addEventListener("click", replayLast);
document.querySelector("#undoButton").addEventListener("click", undoLastAdd);
document.querySelector("#clearQueueButton").addEventListener("click", clearQueue);
document.querySelector("#clearDoneButton").addEventListener("click", clearDone);
document.querySelector("#editChildrenButton").addEventListener("click", openEditor);
document.querySelector("#resetChildrenButton").addEventListener("click", resetChildren);
editorDialog.addEventListener("close", saveEditorChanges);

render();

function loadState() {
  const fallback = {
    children: defaultChildren,
    queue: [],
    active: [],
    done: [],
    lastAddedId: null,
    lastSpoken: null,
  };

  try {
    const saved = JSON.parse(localStorage.getItem(STORAGE_KEY));
    if (!saved || !Array.isArray(saved.children)) return fallback;
    return {
      children: saved.children.length ? saved.children : defaultChildren,
      queue: Array.isArray(saved.queue) ? saved.queue : [],
      active: Array.isArray(saved.active) ? saved.active : [],
      done: Array.isArray(saved.done) ? saved.done : [],
      lastAddedId: saved.lastAddedId ?? null,
      lastSpoken: saved.lastSpoken ?? null,
    };
  } catch {
    return fallback;
  }
}

function saveState() {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
}

function render() {
  renderChildren();
  renderQueue();
  renderActive();
  renderDone();
  renderCurrentCall();
  saveState();
}

function renderChildren() {
  childrenCount.textContent = `${state.children.length} 人`;
  childrenGrid.innerHTML = "";

  state.children.forEach((child) => {
    const card = document.createElement("article");
    card.className = "child-card";
    card.style.setProperty("--child-color", child.color);

    const head = document.createElement("div");
    head.className = "child-head";
    head.innerHTML = `
      <div class="avatar">${escapeHtml(child.avatar)}</div>
      <div class="child-name">${escapeHtml(child.name)}</div>
    `;

    const buttons = document.createElement("div");
    buttons.className = "subject-buttons";

    Object.entries(subjects).forEach(([subjectId, subject]) => {
      const button = document.createElement("button");
      button.className = "subject-button";
      button.textContent = subject.label;
      button.style.setProperty("--subject-bg", subject.bg);
      button.style.setProperty("--subject-border", subject.border);
      button.addEventListener("click", () => addToQueue(child.id, subjectId));
      buttons.append(button);
    });

    card.append(head, buttons);
    childrenGrid.append(card);
  });
}

function renderQueue() {
  queueCount.textContent = `${state.queue.length} 条`;
  queueList.innerHTML = "";

  if (state.queue.length === 0) {
    queueList.append(emptyState("当前没有排队"));
    return;
  }

  state.queue.forEach((item, index) => {
    const child = findChild(item.childId);
    const subject = subjects[item.subjectId];
    const row = document.createElement("article");
    row.className = "queue-item";
    row.style.setProperty("--child-color", child.color);
    row.innerHTML = `
      <div class="queue-rank">${index + 1}</div>
      <div class="queue-main">
        <div class="queue-title">${escapeHtml(child.avatar)} ${escapeHtml(child.name)} - ${subject.label}</div>
        <div class="queue-meta">加入时间 ${formatTime(item.createdAt)}</div>
      </div>
    `;

    const actions = document.createElement("div");
    actions.className = "queue-actions";
    actions.append(
      rowButton("往后", () => delayQueueItem(item.id)),
      rowButton("删除", () => removeQueueItem(item.id))
    );
    row.append(actions);
    queueList.append(row);
  });
}

function renderDone() {
  doneCount.textContent = `${state.done.length} 条`;
  doneList.innerHTML = "";

  if (state.done.length === 0) {
    doneList.append(emptyState("今天还没有讲完记录"));
    return;
  }

  state.done.slice().reverse().forEach((item) => {
    const child = item.childSnapshot;
    const subject = subjects[item.subjectId];
    const row = document.createElement("article");
    row.className = "done-item";
    row.style.setProperty("--child-color", child.color);
    row.innerHTML = `
      <div class="avatar">${escapeHtml(child.avatar)}</div>
      <div class="done-main">
        <div class="done-title">${escapeHtml(child.name)} - ${subject.label}</div>
        <div class="done-meta">完成时间 ${formatTime(item.doneAt)}${item.remark ? `｜备注：${escapeHtml(item.remark)}` : ""}</div>
      </div>
    `;
    doneList.append(row);
  });
}

function renderActive() {
  activeCount.textContent = `${state.active.length} 人`;
  activeList.innerHTML = "";

  if (state.active.length === 0) {
    activeList.append(emptyState("现在没有正在讲解的人"));
    return;
  }

  state.active.forEach((item) => {
    const child = item.childSnapshot;
    const subject = subjects[item.subjectId];
    const row = document.createElement("article");
    row.className = "active-item";
    row.style.setProperty("--child-color", child.color);
    row.innerHTML = `
      <div class="avatar">${escapeHtml(child.avatar)}</div>
      <div class="active-main">
        <div class="active-title">${escapeHtml(child.name)} - ${subject.label}</div>
        <div class="active-meta">开始时间 ${formatTime(item.startedAt)}</div>
      </div>
      <div class="remark-box">
        <label for="remark-${item.id}">备注</label>
        <textarea id="remark-${item.id}" data-id="${item.id}" placeholder="例如：字太乱、订正第3题、作文开头">${escapeHtml(item.remark ?? "")}</textarea>
      </div>
    `;

    const textarea = row.querySelector("textarea");
    textarea.addEventListener("input", () => updateActiveRemark(item.id, textarea.value));

    const actions = document.createElement("div");
    actions.className = "queue-actions";
    actions.append(
      rowButton("完成", () => finishActiveItem(item.id)),
      rowButton("退回队列", () => returnActiveToQueue(item.id))
    );
    row.append(actions);
    activeList.append(row);
  });
}

function renderCurrentCall() {
  if (!state.lastSpoken) {
    currentCall.textContent = "还没有播报记录";
    return;
  }

  const subject = subjects[state.lastSpoken.subjectId];
  currentCall.textContent = `刚刚叫到：${state.lastSpoken.childSnapshot.name}，${subject.label}`;
}

function addToQueue(childId, subjectId) {
  const item = {
    id: createId(),
    childId,
    subjectId,
    createdAt: Date.now(),
  };
  state.queue.push(item);
  state.lastAddedId = item.id;
  render();
}

function callNext() {
  if (state.queue.length === 0) return;

  const next = state.queue.shift();
  const child = findChild(next.childId);
  const activeItem = {
    ...next,
    childSnapshot: { name: child.name, avatar: child.avatar, color: child.color },
    startedAt: Date.now(),
    remark: "",
  };

  state.active.push(activeItem);
  state.lastSpoken = activeItem;
  state.lastAddedId = null;
  speak(`${child.name}，${subjects[next.subjectId].label}`);
  render();
}

function replayLast() {
  if (!state.lastSpoken) return;

  const subject = subjects[state.lastSpoken.subjectId];
  speak(`${state.lastSpoken.childSnapshot.name}，${subject.label}`);
}

function undoLastAdd() {
  if (!state.lastAddedId) return;

  const index = state.queue.findIndex((item) => item.id === state.lastAddedId);
  if (index !== -1) {
    state.queue.splice(index, 1);
  }
  state.lastAddedId = null;
  render();
}

function delayQueueItem(itemId) {
  const index = state.queue.findIndex((item) => item.id === itemId);
  if (index === -1 || index === state.queue.length - 1) return;

  const item = state.queue[index];
  state.queue.splice(index, 1);
  state.queue.splice(index + 1, 0, item);
  render();
}

function removeQueueItem(itemId) {
  state.queue = state.queue.filter((item) => item.id !== itemId);
  if (state.lastAddedId === itemId) state.lastAddedId = null;
  render();
}

function clearQueue() {
  state.queue = [];
  state.lastAddedId = null;
  render();
}

function clearDone() {
  state.done = [];
  render();
}

function updateActiveRemark(itemId, remark) {
  const item = state.active.find((activeItem) => activeItem.id === itemId);
  if (!item) return;
  item.remark = remark;
  saveState();
}

function finishActiveItem(itemId) {
  const index = state.active.findIndex((item) => item.id === itemId);
  if (index === -1) return;

  const [item] = state.active.splice(index, 1);
  state.done.push({
    ...item,
    doneAt: Date.now(),
  });
  render();
}

function returnActiveToQueue(itemId) {
  const index = state.active.findIndex((item) => item.id === itemId);
  if (index === -1) return;

  const [item] = state.active.splice(index, 1);
  state.queue.unshift({
    id: item.id,
    childId: item.childId,
    subjectId: item.subjectId,
    createdAt: Date.now(),
  });
  render();
}

function openEditor() {
  renderEditor();
  editorDialog.showModal();
}

function renderEditor() {
  editorList.innerHTML = "";

  state.children.forEach((child, index) => {
    const row = document.createElement("label");
    row.className = "editor-row";
    row.innerHTML = `
      <input aria-label="符号 ${index + 1}" data-field="avatar" data-id="${child.id}" value="${escapeAttribute(child.avatar)}" maxlength="4" />
      <input aria-label="名字 ${index + 1}" data-field="name" data-id="${child.id}" value="${escapeAttribute(child.name)}" />
      <input aria-label="颜色 ${index + 1}" data-field="color" data-id="${child.id}" type="color" value="${child.color}" />
    `;
    editorList.append(row);
  });
}

function saveEditorChanges() {
  const inputs = editorList.querySelectorAll("input");
  inputs.forEach((input) => {
    const child = state.children.find((item) => item.id === input.dataset.id);
    if (!child) return;
    const value = input.value.trim();
    if (input.dataset.field === "name") child.name = value || "未命名";
    if (input.dataset.field === "avatar") child.avatar = value || "○";
    if (input.dataset.field === "color") child.color = value;
  });
  render();
}

function resetChildren() {
  state.children = defaultChildren.map((child) => ({ ...child, id: createId() }));
  state.queue = [];
  state.active = [];
  state.done = [];
  state.lastAddedId = null;
  state.lastSpoken = null;
  renderEditor();
  render();
}

function findChild(childId) {
  return state.children.find((child) => child.id === childId) ?? {
    name: "已删除",
    avatar: "○",
    color: "#94a3b8",
  };
}

function rowButton(text, onClick) {
  const button = document.createElement("button");
  button.className = "row-button";
  button.textContent = text;
  button.addEventListener("click", onClick);
  return button;
}

function emptyState(text) {
  const div = document.createElement("div");
  div.className = "empty-state";
  div.textContent = text;
  return div;
}

function speak(text) {
  if (!("speechSynthesis" in window)) return;
  speechSynthesis.cancel();
  const utterance = new SpeechSynthesisUtterance(text);
  utterance.lang = "zh-CN";
  utterance.rate = 0.95;
  speechSynthesis.speak(utterance);
}

function formatTime(timestamp) {
  return new Intl.DateTimeFormat("zh-CN", {
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit",
  }).format(timestamp);
}

function escapeHtml(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

function escapeAttribute(value) {
  return escapeHtml(value).replaceAll("`", "&#096;");
}

function createId() {
  if (window.crypto?.randomUUID) return window.crypto.randomUUID();
  return `${Date.now()}-${Math.random().toString(16).slice(2)}`;
}
