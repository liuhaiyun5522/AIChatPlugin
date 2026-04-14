package com.ji.aichat

import com.intellij.openapi.project.Project
import com.intellij.ui.components.JBScrollPane
import com.intellij.ui.components.JBTextArea
import java.awt.BorderLayout
import java.awt.Dimension
import java.awt.FlowLayout
import java.awt.event.KeyAdapter
import java.awt.event.KeyEvent
import javax.swing.*

class ChatPanel(private val project: Project) {

    private val chatHistory = JBTextArea().apply {
        isEditable = false
        lineWrap = true
        wrapStyleWord = true
        font = font.deriveFont(13f)
        text = "🤖 AI Chat Assistant ready! Ask me anything.\n\n"
    }

    private val inputField = JBTextArea().apply {
        lineWrap = true
        wrapStyleWord = true
        font = font.deriveFont(13f)
        rows = 3
    }

    private val mainPanel = JPanel(BorderLayout())

    init {
        // Chat history area (scrollable)
        val historyScroll = JBScrollPane(chatHistory).apply {
            verticalScrollBarPolicy = ScrollPaneConstants.VERTICAL_SCROLLBAR_AS_NEEDED
        }

        // Input area
        val inputScroll = JBScrollPane(inputField).apply {
            preferredSize = Dimension(0, 80)
        }

        // Send button
        val sendButton = JButton("Send").apply {
            addActionListener { sendMessage() }
        }

        // Bottom panel: input + button
        val bottomPanel = JPanel(BorderLayout(5, 0)).apply {
            add(inputScroll, BorderLayout.CENTER)
            add(sendButton, BorderLayout.EAST)
        }

        // Ctrl+Enter to send
        inputField.addKeyListener(object : KeyAdapter() {
            override fun keyPressed(e: KeyEvent) {
                if (e.keyCode == KeyEvent.VK_ENTER && e.isControlDown) {
                    sendMessage()
                    e.consume()
                }
            }
        })

        mainPanel.apply {
            add(historyScroll, BorderLayout.CENTER)
            add(bottomPanel, BorderLayout.SOUTH)
        }
    }

    private fun sendMessage() {
        val userMessage = inputField.text.trim()
        if (userMessage.isEmpty()) return

        // Show user message
        appendToChat("👤 You: $userMessage\n\n")
        inputField.text = ""

        // TODO: Replace this with real AI API call (OpenAI, Claude, etc.)
        val aiResponse = generateMockResponse(userMessage)
        appendToChat("🤖 AI: $aiResponse\n\n")
    }

    private fun generateMockResponse(message: String): String {
        // Mock response - replace with actual API call later
        return when {
            message.contains("hello", ignoreCase = true) -> "Hello! How can I help you today?"
            message.contains("help", ignoreCase = true) -> "I'm here to help! You can ask me about your code, debugging, or any programming questions."
            message.contains("code", ignoreCase = true) -> "I'd be happy to help with your code! Please paste the relevant snippet and describe the issue."
            else -> "Thanks for your question: \"$message\"\n\nThis is a demo response. To connect a real AI backend, update the `generateMockResponse` method in ChatPanel.kt with your API call."
        }
    }

    private fun appendToChat(text: String) {
        chatHistory.append(text)
        // Auto-scroll to bottom
        chatHistory.caretPosition = chatHistory.document.length
    }

    fun getContent(): JComponent = mainPanel
}
