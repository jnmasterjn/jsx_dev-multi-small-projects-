//
//  ContentView.swift
//  Emojii
//
//  Created by Janice Shih on 2024/3/3.
//

import SwiftUI

//enum allows to group related values tgt
enum Emoji: String, CaseIterable{
    case 🥧,😍,🧃,😂
}


struct ContentView: View {
    @State var selection: Emoji = .🥧
    
    var body: some View {
        NavigationView{
            VStack{
                //first element in Vstack: Text
                Text(selection.rawValue)
                    .font(.system(size: 150))
                
                //second element in Vstack: Picker
                Picker("Select Emoji", selection: $selection){
                    ForEach(Emoji.allCases, id: \.self) {emoji in
                        Text(emoji.rawValue)
                    }
                }
                .pickerStyle(.wheel)
            }
            .navigationTitle("Emoji")
            .padding(50.0)
        }
    }
}

#Preview{
    ContentView()
}
