//
//  ContentView.swift
//  test
//
//  Created by Janice Shih on 2024/3/2.
//

import SwiftUI

struct ContentView: View {
    var body: some View {
        VStack {
            //add a button
            Button("Tap on me") {
                print("hi")
            }
            //add toggle
            Toggle(isOn: /*@START_MENU_TOKEN@*//*@PLACEHOLDER=Is On@*/.constant(true)/*@END_MENU_TOKEN@*/) {
                /*@START_MENU_TOKEN@*//*@PLACEHOLDER=Label@*/Text("Label")/*@END_MENU_TOKEN@*/
            }
            //add image
            Image("jn")
                .resizable()
                .padding(2.0)
                .imageScale(.small)
                .foregroundColor(.pink)
                .foregroundStyle(.clear)
            Text("hi").italic().padding()
            Text("second line").bold()
        }
        .padding()
    }
}

//MARK: this is for previews
#Preview {
    ContentView()
}
