if (!task || !time) {
    alert("Enter task and time");
    return;
  }

  setTimeout(() => {
    new Notification("Reminder 🔔", {
      body: task
    });
  }, time * 1000);

  alert("Reminder set!");
};

// Register Service Worker
if ("serviceWorker" in navigator) {
  navigator.serviceWorker.register("/firebase-messaging-sw.js")
    .then(() => console.log("Service Worker Registered"))
    .catch(err => console.log(err));
}
