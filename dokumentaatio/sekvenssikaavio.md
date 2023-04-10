sequenceDiagram
    participant User
    participant MindmapApp
    participant UserSelectionScreen
    participant UserManagement
    participant FolderSelectionScreen

    User->>MindmapApp: run()
    MindmapApp->>MindmapApp: show_loading_screen()
    Note over MindmapApp: Show LoadingScreen
    MindmapApp->>MindmapApp: show_user_selection_screen()
    Note over MindmapApp: Show UserSelectionScreen
    User->>UserSelectionScreen: Click "New User" and input "Bob"
    UserSelectionScreen->>UserManagement: create_new_user("Bob")
    UserManagement->>UserManagement: create_user("Bob")
    Note over UserManagement: Add "Bob" button to UserSelectionScreen
    User->>UserManagement: Click "Bob" button
    UserManagement->>MindmapApp: show_folder_selection_screen("Bob")
    MindmapApp->>FolderSelectionScreen: show("Bob")
    Note over MindmapApp: Show FolderSelectionScreen
    User->>FolderSelectionScreen: Click "New Folder" and input "Math"
    FolderSelectionScreen->>FolderSelectionScreen: new_folder()
    Note over FolderSelectionScreen: Create "Math" folder and update folder list
