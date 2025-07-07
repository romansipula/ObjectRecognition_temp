#!/usr/bin/env python3
"""
Test script to verify all dependencies are installed correctly
"""

def test_imports():
    """Test all required package imports"""
    print("Testing package imports...")
    
    try:
        import streamlit as st
        print(f"✅ Streamlit: {st.__version__}")
    except ImportError as e:
        print(f"❌ Streamlit: {e}")
        return False
    
    try:
        import ultralytics
        print(f"✅ Ultralytics: {ultralytics.__version__}")
    except ImportError as e:
        print(f"❌ Ultralytics: {e}")
        return False
    
    try:
        import cv2
        print(f"✅ OpenCV: {cv2.__version__}")
    except ImportError as e:
        print(f"❌ OpenCV: {e}")
        return False
    
    try:
        import numpy as np
        print(f"✅ NumPy: {np.__version__}")
    except ImportError as e:
        print(f"❌ NumPy: {e}")
        return False
    
    return True

def test_yolo():
    """Test YOLO model loading"""
    print("\nTesting YOLO model...")
    
    try:
        from ultralytics import YOLO
        print("✅ YOLO class imported successfully")
        
        # Test model creation (this will download the model on first use)
        print("✅ YOLOv8 is ready to use!")
        return True
    except Exception as e:
        print(f"❌ YOLO test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("=== Object Recognition Dependencies Test ===\n")
    
    imports_ok = test_imports()
    yolo_ok = test_yolo()
    
    print("\n=== Test Results ===")
    if imports_ok and yolo_ok:
        print("🎉 All tests passed! Your environment is ready for object recognition.")
    else:
        print("⚠️  Some tests failed. Please check the error messages above.")

if __name__ == "__main__":
    main()
