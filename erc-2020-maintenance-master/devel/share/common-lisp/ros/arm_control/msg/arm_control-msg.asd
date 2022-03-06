
(cl:in-package :asdf)

(defsystem "arm_control-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "Efforts" :depends-on ("_package_Efforts"))
    (:file "_package_Efforts" :depends-on ("_package"))
  ))