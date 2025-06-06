package com.example.sampleloginandroid

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import com.example.sampleloginandroid.ui.theme.SampleLoginAndroidTheme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            SampleLoginAndroidTheme {
                AppNavigation()
            }
        }
    }
}
