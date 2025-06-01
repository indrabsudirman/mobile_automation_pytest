//
//  HomeView.swift
//  Sample Login iOS
//
//  Created by Indra on 01/06/25.
//

import SwiftUI

struct HomeView: View {
    let email: String

    var body: some View {
        VStack(spacing: 20) {
            Text("Home")
                .font(.largeTitle)
                .bold()
                .accessibilityIdentifier(AccessibilityIdentifier.Home.home)

            Text("Welcome, \(email)")
                .font(.title2)
                .padding(.top, 10)
                .accessibilityIdentifier(AccessibilityIdentifier.Home.message)
        }
        .padding()
        .accessibilityIdentifier("homeScreen")
    }
}


