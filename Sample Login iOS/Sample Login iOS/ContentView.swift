//
//  ContentView.swift
//  Sample Login iOS
//
//  Created by Indra on 31/05/25.
//

import SwiftUI

enum Route: Hashable {
    case home(email: String)
}

struct ContentView: View {
    @State private var email: String = ""
    @State private var password: String = ""
    @State private var loginMessage: String = ""
    @State private var isPasswordVisible: Bool = false
    @State private var path: [Route] = []


    var body: some View {
        NavigationStack(path: $path) {
            VStack(spacing: 20) {
                Text("Welcome")
                    .font(.largeTitle)
                    .bold()
                    .accessibilityIdentifier(AccessibilityIdentifier.Login.welcome)
                
                Text("Login Page")
                    .font(.title)
                    .bold()
                    .accessibilityIdentifier(AccessibilityIdentifier.Login.title)
                
                TextField("Email", text: $email)
                    .autocapitalization(.none)
                    .keyboardType(.emailAddress)
                    .padding()
                    .background(Color(.secondarySystemBackground))
                    .cornerRadius(10)
                    .accessibilityIdentifier(AccessibilityIdentifier.Login.emailField)
                
                HStack {
                    Group {
                        if isPasswordVisible {
                            TextField("Password", text: $password)
                        } else {
                            SecureField("Password", text: $password)
                        }
                    }
                    .autocapitalization(.none)
                    .padding()
                    .accessibilityIdentifier(AccessibilityIdentifier.Login.passwordField)
                    
                    Button(action: {
                        isPasswordVisible.toggle()
                    }) {
                        Image(systemName: isPasswordVisible ? "eye.slash" : "eye")
                            .foregroundColor(.gray)
                    }
                    .padding(.trailing, 10)
                    .accessibilityIdentifier("passwordVisibilityToggle")
                }
                .background(Color(.secondarySystemBackground))
                .cornerRadius(10)
                
                Button(action: login) {
                    Text("Login")
                        .foregroundColor(.white)
                        .frame(maxWidth: .infinity)
                        .padding()
                        .background(Color.blue)
                        .cornerRadius(10)
                        .accessibilityIdentifier(AccessibilityIdentifier.Login.loginButton)
                }
                
                Text(loginMessage)
                    .foregroundColor(.red)
                    .padding(.top, 10)
                    .accessibilityIdentifier(AccessibilityIdentifier.Login.messageText)
            }
            .padding()
            .navigationDestination(for: Route.self) { route in
                        switch route {
                        case .home(let email):
                            HomeView(email: email)
                        }
                    }
        }
    }


    func login() {
        if email.isEmpty || password.isEmpty {
            loginMessage = "Email dan password harus diisi."
        } else if email == "indra.indrabayu@gmail.com" && password == "MyPassword@12345" {
            loginMessage = ""
            path.append(.home(email: email))
        } else {
            loginMessage = "Email atau password salah."
        }
    }
}

#Preview {
    ContentView()
}

