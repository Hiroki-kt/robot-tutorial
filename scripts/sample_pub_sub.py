#! /usr/bin/env python
# -*- coding: utf-8 -*-

import rospy

## もし自分で作ったメッセージのファイルを使いたい場合
#from spring_seminar.msg import Pos
#from spring_seminar.msg import State

## 元々ROSには様々なメッセージファイルが存在します。
## これらのメッセージファイルを用いたほうが楽ですし、
## 他の人にもわかりやすいです。
from std_msgs.msg import Int32
## Int32 data
from geometry_msgs.msg import Point
## Point
## float64 x
## float64 y
## float64 z

###########################################
## 関数定義
###########################################

## Kukaにかかるトルクの値から押されているか引かれているかを計算 → Publish(力の検出の場合)
## 0 : 特に引いても押してもない
## 1 : 押してる
## 2 : 引いてる
'''
def kukaForceAndDirctionPub(data):
    ## それぞれの関節にかかるトルクから力の導出のプログラム
'''

##########################
## コールバック関数
##########################
## kukaからの各関節にかかるトルクの情報を取得後、力に変換
'''
def callbacKuka(data):
    ## Kukaの各関節にかかるトルクのデータを取得
'''

## ARマーカーからの座標の更新。
def callbackPos(data):
    global xPos
    global yPos
    global zPos
    xPos = data.x 
    yPos = data.y 
    zPos = data.z 
    ## デバッグ用
    # rospy.loginfo("AR Marker Position:(x:%s,y:%s,z:%s)", xPos, yPos, zPos)


## 現在のStateを監視
def callbackState(data):
    global state
    state = data.data
    ## デバッグ用
    # rospy.loginfo("OK")

###########################################
## Main関数
###########################################

if __name__ == "__main__":
    ## ノード定義 
    rospy.init_node('sample', anonymous=True)
    
    ## 変数定義
    global dirAndForcePub
    global statePub
    global state
    global xPos
    global yPos
    global zPos
    stateMsg = Int32()

    ## 初期化
    state = 0
    xPos = None
    yPos = None
    zPos = None

    ## Pub,Sub設定
    ## Subscriberはこの設定をするだけで、勝手にそれぞれのCallback関数を
    ## subscibeが届くたびに実行する
    dirAndForcePub = rospy.Publisher('force_and_direction', Int32, queue_size=10)
    statePub = rospy.Publisher('state', Int32, queue_size=10)    
    rospy.Subscriber("position", Point, callbackPos)  
    rospy.Subscriber("state", Int32 , callbackState)
    ## あと、KUKAについての情報をとるSubscriberが必要(トルク測る場合)

    ## モーション作成
    ## Ctl+Cを押すなどしない限り、モーションの作成
    ## プログラム例：蓋を置く動作の作成のための命令。
    while not rospy.is_shutdown():
        ## State == 2 になるまで待つ
        if state == 2 : 
            ## マーカのx,y座標,決められた高さだけz座標を上げた位置にKUKAを移動 
            ## マーカーのポジションにKUKA移動
            ## ハンドを開く。
            ## 開き終わるまで待つ
            ## マーカのx,y座標,決められた高さだけz座標を上げた位置にKUKAを移動 
            ## State = 3 をPublish
            state = 3
            stateMsg.data = state
            rospy.loginfo("State:%s",stateMsg.data)
            statePub.publish(stateMsg)

