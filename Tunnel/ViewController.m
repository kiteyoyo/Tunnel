//
//  ViewController.m
//  Tunnel
//
//  Created by LarryStanley on 2015/10/21.
//  Copyright © 2015年 LarryStanley. All rights reserved.
//

#import "ViewController.h"
#import "Colours.h"


@interface ViewController ()

@end

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];

    // create background gradient
    UIColor *topColor = [UIColor colorFromHexString:@"#556BAF"];
    UIColor *bottomColor = [UIColor colorFromHexString:@"#5B9FCA"];
    
    CAGradientLayer *theViewGradient = [CAGradientLayer layer];
    theViewGradient.colors = [NSArray arrayWithObjects: (id)topColor.CGColor, (id)bottomColor.CGColor, nil];
    theViewGradient.frame = self.view.bounds;
    
    [self.view.layer insertSublayer:theViewGradient atIndex:0];

    // set scroll view
    scrollView = [[UIScrollView alloc] initWithFrame:self.view.frame];
    [self.view addSubview:scrollView];
    
    // set overal label
    UILabel *overAllLabel = [[UILabel alloc] initWithFrame:CGRectMake(0, 0, 0, 0)];
    overAllLabel.text = @"總結";
    overAllLabel.font = [UIFont fontWithName:@"HelveticaNeue-UltraLight" size:26.0f];
    [overAllLabel sizeToFit];
    overAllLabel.frame = CGRectMake(self.view.frame.size.width/2 - overAllLabel.frame.size.width/2, 30, overAllLabel.frame.size.width, overAllLabel.frame.size.height);
    overAllLabel.textColor = [UIColor whiteColor];
    [scrollView addSubview:overAllLabel];
    
    UILabel *rightNowLabel = [[UILabel alloc] initWithFrame:CGRectMake(0, 0, 0, 0)];
    rightNowLabel.text = @"目前雪隧狀況";
    rightNowLabel.font = [UIFont fontWithName:@"HelveticaNeue-UltraLight" size:20.0f];
    [rightNowLabel sizeToFit];
    rightNowLabel.frame = CGRectMake(10, self.view.frame.size.height/5*3, rightNowLabel.frame.size.width, rightNowLabel.frame.size.height);
    rightNowLabel.textColor = [UIColor whiteColor];
    [scrollView addSubview:rightNowLabel];
    
    UIView *line = [[UIView alloc] initWithFrame:CGRectMake( 10, rightNowLabel.frame.size.height + rightNowLabel.frame.origin.y + 5, self.view.frame.size.width/5 * 3, 1)];
    line.backgroundColor = [UIColor whiteColor];
    [scrollView addSubview:line];
    
    UILabel *northSpeedLabel = [[UILabel alloc] initWithFrame:CGRectMake(0, 0, 0, 0)];
    northSpeedLabel.text = @"64";
    northSpeedLabel.font = [UIFont fontWithName:@"HelveticaNeue-UltraLight" size:44.0f];
    [northSpeedLabel sizeToFit];
    northSpeedLabel.frame = CGRectMake(10, line.frame.size.height + line.frame.origin.y + 5, northSpeedLabel.frame.size.width, northSpeedLabel.frame.size.height);
    northSpeedLabel.textColor = [UIColor whiteColor];
    [scrollView addSubview:northSpeedLabel];
    
    UILabel *northUnitLabel = [[UILabel alloc] initWithFrame:CGRectMake(0, 0, 0, 0)];
    northUnitLabel.text = @"北上\nkm/hr";
    northUnitLabel.numberOfLines = 0;
    northUnitLabel.font = [UIFont fontWithName:@"HelveticaNeue-UltraLight" size:16];
    [northUnitLabel sizeToFit];
    northUnitLabel.frame = CGRectMake( northSpeedLabel.frame.size.width + northSpeedLabel.frame.origin.x + 5, northSpeedLabel.frame.size.height + northSpeedLabel.frame.origin.y - northUnitLabel.frame.size.height, northUnitLabel.frame.size.width, northUnitLabel.frame.size.height);
    northUnitLabel.textColor = [UIColor whiteColor];
    [scrollView addSubview:northUnitLabel];
    
    UILabel *southSpeedLabel = [[UILabel alloc] initWithFrame:CGRectMake(0, 0, 0, 0)];
    southSpeedLabel.text = @"56";
    southSpeedLabel.font = [UIFont fontWithName:@"HelveticaNeue-UltraLight" size:44.0f];
    [southSpeedLabel sizeToFit];
    southSpeedLabel.frame = CGRectMake(northUnitLabel.frame.size.width + northUnitLabel.frame.origin.x + 10, line.frame.size.height + line.frame.origin.y + 5, southSpeedLabel.frame.size.width, southSpeedLabel.frame.size.height);
    southSpeedLabel.textColor = [UIColor whiteColor];
    [scrollView addSubview:southSpeedLabel];
    
    UILabel *southUnitLabel = [[UILabel alloc] initWithFrame:CGRectMake(0, 0, 0, 0)];
    southUnitLabel.text = @"南下\nkm/hr";
    southUnitLabel.numberOfLines = 0;
    southUnitLabel.font = [UIFont fontWithName:@"HelveticaNeue-UltraLight" size:16];
    [southUnitLabel sizeToFit];
    southUnitLabel.frame = CGRectMake( southSpeedLabel.frame.size.width + southSpeedLabel.frame.origin.x + 5, southSpeedLabel.frame.size.height + southSpeedLabel.frame.origin.y - southUnitLabel.frame.size.height, southUnitLabel.frame.size.width, southUnitLabel.frame.size.height);
    southUnitLabel.textColor = [UIColor whiteColor];
    [scrollView addSubview:southUnitLabel];

    UILabel *estimateTextLabel = [[UILabel alloc] initWithFrame:CGRectMake(0, 0, 0, 0)];
    estimateTextLabel.text = @"目前位置抵達宜蘭預估時間";
    estimateTextLabel.font = [UIFont fontWithName:@"HelveticaNeue-UltraLight" size:18.0f];
    [estimateTextLabel sizeToFit];
    estimateTextLabel.frame = CGRectMake(10, southSpeedLabel.frame.size.height + southSpeedLabel.frame.origin.y + 20, estimateTextLabel.frame.size.width, estimateTextLabel.frame.size.height);
    estimateTextLabel.textColor = [UIColor whiteColor];
    [scrollView addSubview:estimateTextLabel];
    
    UILabel *estimateTimeLabel = [[UILabel alloc] initWithFrame:CGRectMake(0, 0, 0, 0)];
    estimateTimeLabel.text = @"127";
    estimateTimeLabel.font = [UIFont fontWithName:@"HelveticaNeue-UltraLight" size:72.0f];
    [estimateTimeLabel sizeToFit];
    estimateTimeLabel.frame = CGRectMake(10, estimateTextLabel.frame.size.height + estimateTextLabel.frame.origin.y + 10, estimateTimeLabel.frame.size.width, estimateTimeLabel.frame.size.height);
    estimateTimeLabel.textColor = [UIColor whiteColor];
    [scrollView addSubview:estimateTimeLabel];
    
    UILabel *estimateMinuteLabel = [[UILabel alloc] initWithFrame:CGRectMake(0, 0, 0, 0)];
    estimateMinuteLabel.text = @"分鐘";
    estimateMinuteLabel.font = [UIFont fontWithName:@"HelveticaNeue-UltraLight" size:18.0f];
    [estimateMinuteLabel sizeToFit];
    estimateMinuteLabel.frame = CGRectMake(estimateTimeLabel.frame.size.width + estimateTimeLabel.frame.origin.x + 10, estimateTimeLabel.frame.size.height + estimateTimeLabel.frame.origin.y - estimateMinuteLabel.frame.size.height - 10, estimateMinuteLabel.frame.size.width, estimateMinuteLabel.frame.size.height);
    estimateMinuteLabel.textColor = [UIColor whiteColor];
    [scrollView addSubview:estimateMinuteLabel];
}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

@end
