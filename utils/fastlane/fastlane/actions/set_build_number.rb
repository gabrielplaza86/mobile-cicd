module Fastlane
    module Actions
  
      class SetBuildNumberAction < Action
        
        def self.run(params)
          sh "(sed -i '' -e \"s/CURRENT_PROJECT_VERSION \= [^\;]*\;/CURRENT_PROJECT_VERSION = #{params[:build_number]};/\" #{params[:xcodeproj]}/project.pbxproj)"
        end
  
        #####################################################
        # @!group Documentation
        #####################################################
  
        def self.description
          "Updates Project Build Number."
        end
  
        def self.details
          "Modifies CURRENT_PROJECT_VERSION from the project replacing it with the input build number"
        end
  
        def self.available_options
          [
            FastlaneCore::ConfigItem.new(key: :build_number,
                                         description: "Build number to be set", 
                                         verify_block: proc do |value|
                                            UI.user_error!("No build number given, pass using `build_number: 'X'`") unless (value and not value.empty?)
                                         end),
            FastlaneCore::ConfigItem.new(key: :xcodeproj,
                                         description: "Location where the xcodeproj is from this file", 
                                         verify_block: proc do |value|
                                            UI.user_error!("No xcodeproj given, pass using `xcodeproj: 'xcodeproj'`") unless (value and not value.empty?)
                                         end),                                       
          ]
        end
  
        def self.is_supported?(platform)
          platform == :ios
        end
  
      end
    end
  end
